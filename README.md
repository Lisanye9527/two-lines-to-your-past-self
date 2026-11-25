# Two Lines to Your Past Self

An entry for the make.fun bounty
[Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca).

The program (`main.py`, Python 3, standard library only) writes two
lines of text to `/output/entry.txt`: a warning to the writer's past
self about one specific moment, and one sentence on why that moment
mattered.

> Do not say 'ship it' just because the deploy went green on the first try at 6 p.m. on a Friday.
> That one easy win is why you stopped reading the logs, and the next failure waited in them for weeks, written out in plain sight, before you ever looked.

The text is a constant in the program, so every run writes exactly
the same bytes. The program checks the text against the bounty gate
(1–280 characters, exactly two lines, not only white space) before
writing and fails loudly if it ever drifts out of bounds.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Licensed under the MIT License (see `LICENSE`).
