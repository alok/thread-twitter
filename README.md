## What it does

Read a Twitter thread as a Markdown file, with indentation to indicate
which tweet is in reply to which.

See `example.md` for, well, an example.

Consecutive tweets by the same user are flattened onto the same level of
indentation since they're probably meant as continuations of a single
thought.

## Dependencies

You'll need:

-   [python-twitter](https://github.com/bear/python-twitter).
-   Twitter API keys (which requires a developer account. See
    [here](https://python-twitter.readthedocs.io/en/latest/getting_started.html).
-   Python 3.7+

You must also define these environment variables for the script to pick
up your API keys:

-   `TWITTER_KEY`
-   `TWITTER_SECRET`
-   `TWITTER_TOKEN`
-   `TWITTER_TOKEN_SECREt`

## Usage

The script takes in any amount of status URLs, which have the form
`https://twitter.com/{username}/status/{id}.`

It produces Markdown files in the same directory it's run, with the name
`twitter-{id}.md`.

Here's an example:

``` {.sh}
python3 thread_tweets.py https://twitter.com/Hillelogram/status/1107754119627001859 https://twitter.com/Hillelogram/status/1108549064239599622
```

## Caveats

Apparently the Twitter search API only works for tweets from the last 7
days. Run this script on threads you like sooner rather than later.

If you have any questions, ask me on
[Twitter](https://twitter.com/therevaloksingh) or on the issue tracker.

## TODO

Add proper threading like Mutt has. Maybe even with the fancy arrows it
draws. [This](https://www.jwz.org/doc/threading.html) looks handy.
