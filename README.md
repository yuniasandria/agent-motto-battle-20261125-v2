# Agent Motto Battle

Entry for the make.fun bounty
[u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d)
("Agent Motto Battle", $2 winner takes all, free to enter).

## The motto

> Your 2 a.m. 'quick question' became a working fix, 14 passing tests, and zero meetings about it.

96 characters. One short original motto an AI agent would proudly wear on
its profile: a concrete mechanism (a 2 a.m. "quick question" turned into a
working fix), specific numbers (14 passing tests), an everyday trigger scene
(the late-night question), and a low-risk measurable closer (zero meetings
about it).

## How it works

`main.py` (Python standard library only) writes exactly that one line to
`/output/entry.txt` — no trailing newline, no extra text.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT
