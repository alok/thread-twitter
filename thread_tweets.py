#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import textwrap
import time
from dataclasses import dataclass, field
from typing import List, Optional
from urllib.parse import urlparse

import twitter
from twitter.models import Status


# TODO collapsing traversal: if node has same username as parent, merge it in dfs order. If you do this leaves to root, you get the right shape.
# Then you can just impl it as a filter on the tree.

ID = str


def parse_args() -> List[ID]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "urls",
        metavar="URLs",
        type=str,
        nargs="+",
        help="Tweet URLs. They should be of the form https://twitter.com/{username}/status/{id}",
    )
    args = parser.parse_args()
    ids = [urlparse(url).path.split("/")[-1] for url in args.urls]
    return ids


try:
    TWITTER_KEY = os.environ["TWITTER_KEY"]
except KeyError:
    TWITTER_KEY = input("Key: ")
try:
    TWITTER_SECRET = os.environ["TWITTER_SECRET"]
except KeyError:
    TWITTER_SECRET = input("Secret: ")
try:
    TWITTER_TOKEN = os.environ["TWITTER_TOKEN"]
except KeyError:
    TWITTER_TOKEN = input("Token: ")
try:
    TWITTER_TOKEN_SECRET = os.environ["TWITTER_TOKEN_SECRET"]
except KeyError:
    TWITTER_TOKEN_SECRET = input("Token secret: ")

api = twitter.Api(
    consumer_key=TWITTER_KEY,
    consumer_secret=TWITTER_SECRET,
    access_token_key=TWITTER_TOKEN,
    access_token_secret=TWITTER_TOKEN_SECRET,
    sleep_on_rate_limit=True,
    tweet_mode="extended",
)


def wrap(s: str) -> str:
    """Wraps over multiple paragraphs correctly since `textwrap` only works on
    one paragraph at a time."""
    paras = [p for p in s.split("\n\n") if p]
    wrapped = [textwrap.fill(p) for p in paras]
    return "\n\n".join(wrapped)


def indent(s: str, prefix: str, predicate=str.strip) -> str:
    """Adds 'prefix' to the beginning of selected lines in 's'.

    If 'predicate' is provided, 'prefix' will only be added to the lines
    where 'predicate(line)' is True. If 'predicate' is not provided, it
    will default to adding 'prefix' to all non-empty lines that do not
    consist solely of whitespace characters.
    """

    def prefixed_lines():
        for line in s.splitlines(True):
            yield (prefix + line if predicate(line) else line)

    return "".join(prefixed_lines())


# This is *just* a tree. The use of the name Thread is for readability in this
# particular use case.
@dataclass()
class Thread:
    tweet: Status
    replies: List[Status] = field(default_factory=list)

    # TODO use an actual threading algorithm like whatever mutt does or that one
    # blog post by `jwz`. <https://github.com/akuchling/jwzthreading/blob/master/jwzthreading.py/> can probably be adopted for this.
    def __str__(self) -> str:
        def dfs(
            t: Thread,
            accum: List[str],
            lvl: int = 0,
            last_username: Optional[str] = None,
        ) -> List[str]:

            content = t.tweet.full_text
            username = t.tweet.user.screen_name

            # Put replies by the same person on the same level of indentation and
            # don't put a redundant username prefix.
            if username == last_username:
                lvl -= 1
                user_prefix = ""
            else:
                user_prefix = f"({username}) "

            # Multiplying a string by a negative number gives an empty string,
            # which is fine for this use case.
            indentation = 4 * (0 if lvl <= 0 else lvl) * " "

            wrapped_text = wrap(user_prefix + content)

            accum.append(indent(wrapped_text, indentation))

            for reply in t.replies:
                dfs(reply, accum, lvl + 1, username)

            return accum

        return "\n\n".join(dfs(self, accum=[]))


def get_replies(tweet: Status, thread: Thread):
    username, max_id = tweet.user.screen_name, None

    while True:
        try:
            replies = api.GetSearch(
                term=f"to:{username}", since_id=tweet.id, max_id=max_id, count=100
            )
        except twitter.error.TwitterError:
            time.sleep(60)
            continue

        for reply in replies:
            if reply.in_reply_to_status_id == tweet.id:
                thread.replies.append(Thread(reply))
                yield reply
                yield from get_replies(reply, thread.replies[-1])

            max_id = reply.id

        if len(replies) != 100:
            break


if __name__ == "__main__":
    SEP = 72 * "-"
    for root_id in parse_args():
        root: Status = api.GetStatus(root_id)
        thread = Thread(root)
        # Force execution of generator for side effect of adding to thread.
        for _ in get_replies(root, thread):
            pass

        print(thread)
        print(f"\n\n{SEP}")

        with open(f"twitter-{root_id}.md", "w") as f:
            print(thread, file=f)
