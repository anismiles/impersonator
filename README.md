# Impersonator

Impersonator is an agent skill that distills how a person thinks into a new skill. You give it a name. It researches the person, extracts the mental models and decision rules, and writes a perspective skill. That skill then critiques your plans, reasons about your problems, and pushes back the way the person does.

The output does not copy what the person said. It captures how the person thinks.

## What you get

A run produces one folder for the person:

```
.claude/skills/<person>-perspective/
├── SKILL.md              the perspective skill
└── references/
    ├── research/         research notes, one file per dimension, with sources
    └── sources/          primary material (books you own, transcripts, articles)
```

The perspective skill contains these parts:

- Mental models (3 to 7). Each model has evidence from at least two contexts and a statement of its failure conditions.
- Decision heuristics (5 to 10). Each heuristic is an "if X, then Y" rule with a real case.
- An expression profile: sentence style, vocabulary, rhythm, humor, certainty, and citation habits.
- Values, anti-patterns, and internal tensions.
- Honest boundaries: what the skill cannot do, and the research date.
- A research workflow. The persona looks up facts before it answers a factual question.

## Two response modes

Each generated skill has two modes, and the user can switch between them.

- Advisor mode thinks with the person's models but speaks in a plain voice. It names the model behind each main point. Use this mode for critique and decisions.
- Role-play mode answers as the person, in the first person, with the person's style. It gives a disclaimer once and has an exit phrase.

The default mode comes from the purpose that you choose at the start. A thinking advisor gets Advisor mode. Role-play gets Role-play mode.

## Install

Copy the folder into the skills folder of your agent. For Claude Code:

```bash
cp -R impersonator ~/.claude/skills/impersonator
```

Other runtimes that support agent skills use their own skills folder. The skill is plain Markdown with YAML frontmatter, plus four helper scripts. The scripts need Python 3. The subtitle script also needs `yt-dlp`.

## Use

Tell your agent one of these:

```
Distill Cedric Chin
Create a Richard Feynman perspective skill
I want to make better business decisions. Who should I learn from?
Update the Cedric Chin skill
```

A clear name starts the direct path. A vague need starts a short diagnosis. The diagnosis suggests two or three candidates, each with its limits.

## How it works

1. Clarify. The skill settles the person, the focus, the purpose, any local material, and the cost tier.
2. Research. Up to six agents work in parallel on writings, long conversations, short-form expression, criticism by others, decisions, and a timeline. Each agent saves its notes with sources.
3. Review. You see a table of the research and approve it, or ask for more.
4. Extract. A triple test sorts ideas into mental models, heuristics, or noise. The three tests are recurrence across domains, the power to predict new positions, and distinctiveness.
5. Review. You see the extracted models and approve them.
6. Build. The skill fills a fixed template.
7. Test. A script checks the content. Separate agents then test known positions, an edge case, the voice, and a baseline comparison.
8. Refine. Two reviewer agents suggest changes, and you approve them.

Each checkpoint offers defaults, so a checkpoint does not stall the work.

## Cost tiers

A full run is a long task with many agents and searches. On a top model, one run can cost tens of dollars.

| Tier | Research | Use it for |
|------|----------|------------|
| Quick | 3 dimensions, about 5 sources each | A first try, a little-known person, a small budget |
| Standard | All 6 dimensions | Most cases (default) |
| Deep | 6 dimensions plus full primary material | A skill that you plan to share |

## Test results

We tested the method with blind judges on business scenarios that had hidden flaws. Each test compared three advisors: the generated skill, a plain "think like this person" prompt, and a neutral advisor.

| Person | Generated skill | Plain prompt | Neutral advisor |
|--------|----------------:|-------------:|----------------:|
| Paul Graham (very famous) | 94% of flaws found | 94% | 88% |
| Cedric Chin (less famous) | 91% of flaws found | 82% | 77% |

For a very famous person, the base model already knows the ideas, so the skill adds little. For a less famous person, the skill adds real reasoning that a plain prompt misses. In a separate test with the writing style removed, a blind judge still identified which thinker wrote 56 of 60 critiques. The personas reason differently, not only in voice.

These tests are small: 12 scenarios per test, and judges from the same model family. Treat them as a pilot, not as proof.

## Limits and responsible use

- A generated skill infers views from public material. It does not speak for the person.
- The skill cannot predict how the person reacts to a truly new problem.
- Public statements and private views can differ.
- The skill knows nothing after its research date. Update it from time to time.
- For a living private person, use only material that the person agreed to share.
- Do not use a generated skill to deceive people about who is speaking.

---
_Impersonator is derived from the works of `alchaincyf`_
