(Hillelogram) When I defended up-front design, many people accused me
of not "really" doing up-front design, because I was using it "a long
time into the project" and because I had already "iterated on it".

This is both a straw-man view of what "up-front" means... and
completely ahistorical.

What do I mean by "up-front" design? It means, before you start
coding, you dedicate time to planning out what you are going to do. I
usually do this with formal specifications, but that's not the only
way.

Critically, it's not "planning everything". It's not the whole system.

In other words, UFD does not at all contrast with iteration. If your
sprints are two weeks, they can stay two weeks, except now you spend
the beginning of those two weeks thinking through what you'll do with
the rest.

People STRENUOUSLY disagreed with this.

    (_mrc) @Hillelogram My exp with 2 wk sprints is they’re filled with
    work that has been estimated but not designed. Tends to work well for
    boring work that has been done lots before, otherwise “winging”
    planning/design is encouraged (TDD As Design🤮). Do you have a diff
    experience mixing UFD+sprints?

They said that wasn't up-front: doing UFD meant planning out your
entire system first, and then coding it all. Since I wasn't doing
that, I'm not "really" doing up-front design and my arguments are
bull.

But here's the thing: that's NOT what design experts advocated!

Sure, Waterfall (we THINK- it's unclear) tried to minimize movement
between the phases, but the cutting-edge design world quickly
abandoned it. Pretty much every book or paper on design I've read past
1980 strongly advocates iteration, even the "up-front" people.

    (lhochstein) @Hillelogram Survey article co-authored by my advisor
    dates it way back: https://t.co/O3uOmAfL5K

        (parlar) @lhochstein @Hillelogram That was an excellent article!

        (Hillelogram) @lhochstein I haven't read more than a couple design
        papers dating before 1980, so I didn't want to assume anything about
        them :)

I'm looking at Stavely's Cleanroom, @Grady_Booch's OOD, Jacobson's
OOSE, Cook's Syntropy, Boehm's Spiral model, heck, even Praxis's
Correct by Construction all saw continual iteration as necessary and
desirable. Up-front designers _assumed_ you'd be doing incremental
development!

Okay I'm pretty sure RUP didn't, and a lot of companies following
design methods didn't... but are you going to judge a discipline by
how the enterprise butchers it? By the same logic, to be "Agile" you
gotta have a scrum master!

    (herrwieger) @Hillelogram RUP is incrementally. Its one of its core
    charcteristics...

    @Hillelogram from „The Rational Unified Process An Introduction“ from
    @pbpk https://t.co/gBxARd6XzA

    (etscrivner) @Hillelogram RUP itself I’m pretty sure recommended
    sketching an architecture as a prerequisite for implementation

There's this weird myth now that up-front design is incompatible with
agility. That was never the case. People were always trying to find
the right balance between the two. Apparently we somehow stopped- now
if you're up-front designing, you ~oBvIoUsLy~ aren't iterating.

I don't want us to stop iterating. I just want us to stop thinking of
up-front design as heretical.

    (gregmcintyre) @Hillelogram Yes! Thank you for saying so. A lot of
    accusations levelled at agile are similarly fuelled by overly
    simplistic, black and white notions of it.

    (dianamontalion) @Hillelogram *No* upfront design makes as much
    financial sense to me as walking onto a random car lot and buying any
    random car, just so you got sh*t done.

    (samolenkov) @Hillelogram Some design always takes place. In any
    project. If the design is weak and incomplete then the team round the
    circles fixing issues arriving with not dropping rate.

    (ssmusoke) @Hillelogram RUP did play well with up-front design as each
    cycle started with inception phase (planning/design) and ended with
    transition which was collecting feeback, retrospectives to feed the
    inception phase of the next cycle.

    Basically Up-front design to start each cycle

        (Hillelogram) @ssmusoke I mean like I don't know if RUP did constant
        iteration on having constantly completed versions of the code

            (ssmusoke) @Hillelogram Oh yes it was expected at the end of each
            cycle, at least as far as the organization that I worked with did.

                (Hillelogram) @ssmusoke Ooh, that's good to know! Yeah I guess I
                shouldn't be surprised, given that the Three Amigos were all fans of
                iterative development

    (vanlightly) @Hillelogram I wish people could stop being absolutist
    about anything. These absolutists stiffle freedom to think and debate
    through dogma.  They use their dogma as a weapon, if unchallenged,
    people end up self-censoring and stop thinking for themselves.

    (pressron) @Hillelogram I would go further. I want us to stop thinking
    about code as the most important part of programming and software.

    @Hillelogram It's quite easy for me to imagine programming computers
    without writing *any* code, and all the interesting and important
    parts of the work would be largely the same -- gathering requirements,
    designing, debugging, profiling --except there would be no code at
    all.

    @Hillelogram If we compared programming to writing, code wouldn't be
    the words; it's the ink.

    (faassen) @Hillelogram There is a bit of a grey area here. I often
    stop and think carefully and make a plan before I modify code. Is that
    design or iterative development? Is that is considered heretical by
    anyone? Or do people only shout "heresy!" if you use formal methods to
    help you think?

        (Hillelogram) @faassen Probably depends on the local culture. I've
        seen people go "yeah we drive our TDD with sequence diagrams" and
        people who've called me a filthy liar because I said I support TDD but
        also like code contracts

            (craigjbass) @Hillelogram @faassen The first step of TDD is to think.
            https://t.co/kzzrgskD26

                (faassen) @craigjbass @Hillelogram It's such a small step as described
                but it involves so, so much hidden under the surface. The rest of the
                diagram is trivial in comparison.

                    (craigjbass) @faassen @Hillelogram It can mean the difference between
                    bubble sort and quick sort! If you are tackling that particular Kata.

                (Hillelogram) @craigjbass @faassen Right, but is it "think about your
                next test" or "think about the next ten tests and how the next one
                will fit into that plan?"

                    (faassen) @Hillelogram @craigjbass Or (gasp) not think about the tests
                    but where the code is and where it might be going?

                    (craigjbass) @Hillelogram @faassen As part of TDD - just the next
                    test.

                    I don’t practice TDD on its own, I practice ATDD .. that “A” forces me
                    to consider the design of up to around 7~ different modules, each of
                    which will need their own unit tests.

                    @Hillelogram @faassen The boundaries between those units have got to
                    work for both things which are testable by TDD and stuff that isn’t.

            (faassen) @Hillelogram Many local cultures haven't even considered the
            matter, I suspect. I am currently teaching TDD and I have to remind
            people to stop and think and carefully consider function design (the
            signature, though the types aren't explicit in Python) before they
            start typing.

                (Hillelogram) @faassen I think my favorite TDD deliberate practice was
                a pairing exercise between @arsduo and me where we both tried to take
                the "make the smallest possible change to fix" to extreme lengths,
                like he eventually started abusing a deterministic ordering quirk in
                Mocha to "pass" the test

                @faassen @arsduo Not actually all that relevant but it's a funny story
                about improving TDD skills and I like bragging about my coworkers

            @Hillelogram I think that might also inform this discussion. Someone
            advocating more careful design using TDD in an environment where it is
            new might feel throwing in other methods is a distraction.

            @Hillelogram "I am trying to teach iterative design and don't distract
            them with other approaches. I'd be happy if everyone even did this as
            in many contexts it's enough"

                (Hillelogram) @faassen I totally empathize with that. Usually when I
                give a talk on formal methods or generative testing I start with "are
                you unit testing? If not that's gonna be a way better skill to learn
                than this"

                    (faassen) @Hillelogram Be careful with that question. There are many
                    teams who would say "yes we are unit testing" because they write
                    integration tests after coding using a library called "unit test".
                    Valuable to be sure but far from TDD.

            @Hillelogram You come from a perspective of teams where people already
            have this high level TDD skill, but might be speaking to evangelists
            who are trying to spread it in the first place. And there are
            certainly many developers who don't practice TDD.

                (Hillelogram) @faassen I think part of my frustration is that even
                with teams that are experienced with TDD, and people who evangelize
                TDD, they personally think up-front design is silly. Not everyone, but
                enough to make me sad

        @faassen I feel like there's a tipping point here, but I have no idea
        where it is. FM is definitely past it, whiteboard free-diagraming is
        definitely not, I don't know where the gray zone is. Maybe flyweights?
        State machines? Somewhere in the ballpark of "non code artifacts"

        @faassen Yeah it seems that the gray zone is where you're generating
        permanent output that isn't part of the codebase. If so I'd predict
        that functional assertion comments and documentation-driven
        development are "too far".

            (faassen) @Hillelogram I would have thought that technical
            documentation (with executable assertions possibly) driven development
            would be a good way to sneak in this style of thinking in a group that
            already practices TDD. It didn't seem a big leap to me when I did it
            in the past.

    (utterlymundane) @Hillelogram I think it’s the same kind of reflexive
    approach that leads to technology absolutism (some times your data is
    genuinely beat modeled relationally, an RDBMS is fine). There are lots
    of project management techniques, and you should choose the ones that
    reflect your project.

    @Hillelogram My mindset is that your PM/design prices should reflect
    the cost of changing your plans, and the cost of deciding to scrap the
    project. Adding SaaS features? Use your custom scrum-lite, my friend!
    Building a skyscraper? Maybe your process for change needs a tad more
    rigor.

    @Hillelogram To be clear - this is agreeing with you. Almost no
    project has completely scrapping a design as free: so mostly one just
    won’t scrap bad designs until you incur a lot of pain! A good process
    should ensure enough up front design to avoid this cost.

    (jitterted) @Hillelogram I learned that it was BIG up-front design
    that was the problem, i.e., spending months writing specs and digrams,
    and no coding at all. The XP community always had design mechanisms
    (e.g., CRC cards, sequence diagrams) that were done before coding.

    (JoelMcCracken) @Hillelogram The way I understood agile, there was
    always an idea of doing the simplest thing that could possibly work at
    each iteration -- but that means coming up with a *plan* for an
    implementation that could possibly work!

    (twybv) @Hillelogram Can't agree more on this!
