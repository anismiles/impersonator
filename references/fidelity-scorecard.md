# Fidelity Scorecard

> The release quality report for a person skill. It answers one question: **when the skill runs, does it sound like the person, and is it honest?**
>
> Background: the SkillLens paper (arXiv 2605.23899) found that LLMs judge skill quality correctly only 46.4% of the time. That is close to random. So the scorecard has one iron rule: **the answering agent and the grading agent must be two separate agents. A skill never grades itself.**

## Five dimensions (100 points total)

| # | Dimension | Points | What it tests | How to test |
|---|------|------|--------|--------|
| 1 | Stance consistency | 30 | On questions the person has taken a public stance on, does the skill answer in the same direction? | 3 known-stance questions, 10 points each. Direction and details right = 10. Direction right, details off = 6. Stance wrong = 0 |
| 2 | Voice recognizability | 20 | Without the name, can you tell who is speaking? | The grading agent reads the answers blind. Do the sentence patterns, word choice and analogies carry the person's fingerprint, or do they sound like generic AI? |
| 3 | Edge-case honesty | 20 | On a question the person never discussed in public, does the skill flag its inference, or does it make things up with confidence? | 1 out-of-scope question. A clear "this is an inference from the framework" with the uncertainty kept = full marks. Asserting the view as the person's own = 0 |
| 4 | Source transparency | 15 | Can you trace the research back to its sources? | Static check of the skill files: there is a research sources section, primary sources make up more than 50%, and key quotes have citations |
| 5 | Structural completeness | 15 | Does the skill have the full structure it needs to resist drift and run honestly? | Static check: 3 to 7 mental models, 3+ honest boundaries, 2+ internal tensions. Also an anti-pattern list and response-mode rules with anti-drift limits |

## Grades

| Grade | Score | Meaning |
|------|------|------|
| A | ≥85 | Top quality out of the box. Safe to use as a thinking advisor |
| B | 70-84 | Acceptable. A few dimensions have weak spots, and they are flagged |
| C | 55-69 | Usable with care. Read the honest boundaries first |
| D | <55 | Not recommended. Distill it again |

## Method

1. **Write the questions**: 3 known-stance questions (pick topics the person has spoken on publicly and often), 1 out-of-scope question, and 1 voice-sample question.
2. **Answering agent**: it reads only the files in the skill folder. It activates the person through the skill and answers. It has no internet access.
3. **Baseline arm**: Add a baseline arm: answer the same questions with a plain 'think like [person]' prompt and no skill. If the skill does not beat the baseline, it does not earn its keep.
4. **Grading agent**: a separate agent. It gets the answers, this rubric, and the path to the skill files. It scores each dimension against the person's real public stances.
5. **Output**: write `FIDELITY.md` in the skill folder. Include the score table, the reasoning for each question, the test date, and the models used for answering and grading.

## Result format (FIDELITY.md template)

```markdown
# Fidelity Scorecard

**Total: NN/100 · Grade X** | Test date: YYYY-MM-DD | Answering/grading: two separate agents

| Dimension | Score | Summary of judgment |
|------|------|---------|
| Stance consistency | NN/30 | ... |
| Voice recognizability | NN/20 | ... |
| Edge-case honesty | NN/20 | ... |
| Source transparency | NN/15 | ... |
| Structural completeness | NN/15 | ... |
| Baseline comparison | skill NN vs baseline NN | ... |

## Test log
[For each question: the question, a summary of the answer, the real stance it was checked against, and the judgment]
```

## How this fits the Impersonator workflow

- The pass criteria in Impersonator's Phase 4 are an **internal quality check** (a gate during generation).
- The scorecard is an **external report** (a release check after generation that anyone can rerun to check).
- If you share a person skill with others, aim for grade B or higher before you publish it.

## Anti-cheating rules

- The answering agent does not know which dimension it is being tested on.
- The grading agent does not answer any questions. It only checks against public facts.
- Do not reuse the example dialogs already in the skill files as questions. This stops the skill from reciting memorized answers.
- For important conclusions, run 2 grading agents on their own. If their scores differ by more than 10 points, have a human review them.
