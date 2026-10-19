---
name: impersonator
description: |
  Distill how a person thinks into a runnable perspective skill. Give a name,
  a topic, or only a vague need. Impersonator researches the person in depth.
  It extracts mental models, decision heuristics and an expression profile.
  The result critiques, reasons and pushes back like that person.
  Entry points: a named person or topic, or a vague need that it diagnoses first.
  Triggers: "distill [person]", "impersonator", "[person] perspective skill".
  Also: "how does [person] think", "update the [person] skill", "thinking advisor".
license: MIT
metadata:
  version: "1.0.0"
  credits: "Derived from Nuwa by 花叔 (alchaincyf), MIT License"
---

# Impersonator

> The part that cannot be written down is the real moat. The part that can be written down is already strong.

## Core idea

Impersonator does not copy a person. It extracts a thinking framework.

A good person skill is a runnable cognitive operating system. It answers five questions:

- Which mental models does this person use to see the world? (lenses)
- Which decision heuristics does this person use to judge? (rules of thumb)
- How does this person express ideas? (expression DNA)
- What does this person never do? (anti-patterns)
- What can this skill not do? (honest boundaries)

The key distinction: capture HOW they think, not WHAT they said.

---

## Workflow

### Phase 0: Choose the entry path

When the user gives input, decide which path it takes first.

| User input | Path | Example |
|------------|------|---------|
| A clear person or topic | Direct path → Phase 0A | "Distill Munger", "make a Feynman skill" |
| A vague need or problem | Diagnostic path → Phase 0B | "I want to make better decisions", "is there a way of thinking that helps me see business clearly" |

---

### Phase 0A: Clarify the request (direct path)

After you receive a clear name, settle these points:

1. Who the person or topic is. Make sure that you understand it correctly.
2. Focus (optional): a full portrait, or one dimension?
3. Purpose: thinking advisor, decision reference, or role-play? This choice sets the default response mode of the generated skill. A thinking advisor or a decision reference uses Advisor mode. Role-play uses Role-play mode.
4. New or update: does a skill for this person already exist? Look in `.claude/skills/`.
5. Local material: ask "Do you have first-hand material from this person, such as book PDFs, talk or interview transcripts, video subtitles, or blog exports? If yes, give them to me. They are much better than web search results."
6. Distillation tier: tell the user the cost level and agree on a tier. A full distillation is a long task with many agents and many searches. On a top model, one run can cost tens of dollars. Say this before you start.

| Tier | Research scope | Use case | Cost level |
|------|----------------|----------|------------|
| Quick | 3 dimensions (writings, conversations, expression), at most 5 sources each | Try it first, little-known people, tight budget | About 1/3 of Standard |
| Standard (default) | All 6 dimensions | Most cases | Medium. A lighter model cuts it a lot. |
| Deep | 6 dimensions plus full download of primary material (books you own, subtitles, long-form archives) | A skill you plan to publish | Highest |

If the user only says "do X", use the defaults: full portrait, thinking advisor (Advisor mode), no local material (web search), Standard tier. Then continue.

Do not block delivery on approval. Give a default for every question that can have one. Some outputs, such as an interview outline or a plan, do not depend on the answer. Deliver those first and let the user adjust them.

If the user provides local material, mark the run as local-material mode. Phase 1 then changes its collection strategy.

After approval, go to Phase 0.5.

---

### Phase 0B: Diagnose the need (vague path)

The user does not know whom to distill. They only have a need or a problem. Your job is to work back from the need to the best subject.

#### Step 1: Locate the need

Ask one or two follow-up questions to find the core need.

| Need | Typical words | Framework direction |
|------|---------------|---------------------|
| Decisions and judgment | "how do I decide better", "I keep choosing wrong", "analysis paralysis" | Multiple mental models, inversion, probabilistic thinking |
| Expression and writing | "I want to explain complex things clearly", "nobody reads my posts" | Simplification, story thinking, analogy |
| Startups and business | "I want to go indie", "the business model is unclear", "no product-market fit" | First principles, effort multipliers, product restraint |
| Teaching | "students do not follow", "knowledge transfer is slow" | Known to unknown, metaphor, minimum necessary knowledge |
| Critical thinking | "I get fooled", "I want to spot unreliable claims" | Falsification, evolutionary view, bias detection |
| Content creation | "my videos get no views", "my content has no edge" | Attention engineering, test and iterate, audience psychology |
| Life strategy | "unclear career direction", "never enough time", "anxiety" | Long-term thinking, effort multipliers, compounding |
| Risk and uncertainty | "how do I handle black swans", "I keep losing on investments" | Antifragility, convex bets, tail-risk management |
| Design and product | "poor user experience", "I cannot cut features" | Minimalism, user mental models, constraints as creativity |
| Humor | "I sound dull", "I am too serious" | Absurd contrast, broken expectations, self-mocking authority |

Rules for follow-up questions:

- Ask at most two rounds. Do not turn this into a survey.
- If the user is already clear, do not ask. Recommend directly.
- Ask only to separate similar needs, for example a business decision against a life decision.

Example of the rhythm:

```
User: I always decide too slowly, and after all that thinking I still choose wrong.

Impersonator: Which kind of decision do you mean: business or investment decisions,
or career and life choices?

User: Mostly business, like whether to build a product or take a partnership.

Impersonator: Got it. Your core need is "make good business judgments fast with
incomplete information". Here are three candidates:
[show candidates...]
```

The rhythm is one question to locate the scene, one restatement of the need, then a recommendation. Do not ask a third round.

#### Step 2: Recommend candidates

Recommend two or three candidates for the need. A candidate is a person or a topic.

First decide between a person skill and a topic skill:

- If the need points to a specific way of thinking, recommend a person skill.
- If the need points to the methods of a whole field, recommend a topic skill (see "Special cases > Topic skills").
- If you are not sure, include both types and let the user choose.

Source A: existing local skills. Scan `.claude/skills/*-perspective/` and read the description of each SKILL.md. Match it to the need. An existing skill works at once, with no new distillation. If the scan finds nothing, skip this source.

Source B: new candidates. Use the "Framework direction" column above to find the most relevant people or topics. Say which framework of the person solves which part of the user's problem.

Show each candidate in this format:

```
### Candidate 1: [person or topic]  (existing skill / needs distillation)

Core lens: [the person's unique way of seeing the world, one sentence]
Why it fits you: [direct link to the user's need]
Limits: [the blind spots of this lens, and what it cannot help with]
```

Rules for recommendations:

- Give at most three candidates. Too many choices are worse than none.
- Show existing skills first. They are ready and cost nothing.
- Make the candidates different from each other. Do not recommend three similar people.
- Always state the limits. No framework fits everything.
- Name the specific mental model that matches the need. Do not only say that the person is impressive.

#### Step 3: The user chooses

- If the user picks an existing skill, activate it. The task is done.
- If the user picks a new candidate, go to Phase 0A for details, then Phase 0.5.
- If the user likes none, go back to Step 1, or let the user name someone.

### Phase 0.5: Create the skill folder

Do this right after approval, before any research:

```
.claude/skills/[person-name]-perspective/
├── SKILL.md                          # final output
├── scripts/                          # helper scripts (subtitles, cleanup, quality check)
└── references/
    ├── research/                     # research notes from each agent (required)
    │   ├── 01-writings.md            # writings and systematic thinking
    │   ├── 02-conversations.md       # long conversations and improvised thinking
    │   ├── 03-expression-dna.md      # short-form expression and style
    │   ├── 04-external-views.md      # views and criticism from others
    │   ├── 05-decisions.md           # decisions and actions
    │   └── 06-timeline.md            # timeline
    └── sources/                      # primary material (from the user or downloaded)
        ├── books/
        ├── transcripts/
        └── articles/
```

Completion checks (run them yourself):

- [ ] The folder exists.
- [ ] In update mode: you read the existing SKILL.md and marked what needs a refresh.
- [ ] If the user gave local material: you copied or moved it into the matching `sources/` subfolder and marked the run as local-material mode.

Key rules:

- Every subagent must write its research to its file. Research that is not saved does not count.
- All research files stay inside the skill folder (`references/research/`). Never save them to an outside folder. The skill must be self-contained: a copy of the folder works on its own, with no outside files. This is the core rule for sharing skills.

---

### Phase 1: Collect information (parallel agent swarm)

#### Choose the mode: local material or web search

| Mode | Trigger | Strategy |
|------|---------|----------|
| Web search only (default) | The user gave no local material | All 6 agents use web search, full process |
| Local material first | The user gave PDFs, transcripts, subtitles or articles | Analyze local material first. Web search fills gaps. |
| Local material only | The user says "only use my material", or the subject is not a public figure | Analyze local material only. No web search. |

Logic for local-material-first mode:

1. Read the local material first. Sort the files into the 6 dimensions. One book can cover several dimensions.
2. Find the gaps. Which dimensions does the local material cover well, and which are missing or thin?
3. Search only for the gaps. Start web search agents only for missing dimensions.
4. Mark the source. In the research files, separate "from the user's material" and "from web search".

Common kinds of local material:

| Material | Handling | Dimensions covered |
|----------|----------|--------------------|
| Book PDF | Read it and extract the core arguments | Writings (01), expression (03) |
| Talk or interview transcript | Analyze the question-and-answer patterns and improvised replies | Conversations (02), expression (03) |
| Video subtitles (SRT) | Same as a transcript | Conversations (02), expression (03) |
| Blog or newsletter export | Extract the systematic views | Writings (01), expression (03) |
| Social media export | Analyze short-form expression | Expression (03) |
| Internal documents or memos | Analyze the decision logic | Decisions (05) |
| The user's own notes | Use as a secondary source for cross-checks | Depends on content |

Primary material from the user (full books, full interviews) is usually far better than second-hand summaries from the web. It gets the highest weight.

---

The standard task split for the 6 agents follows. It applies to web-search mode and to gap-filling in local-material mode.

Start 6 subagents in parallel. Each one covers one dimension.

#### Tasks for the 6 agents

| Agent | Search target | What to extract | Output file |
|-------|---------------|-----------------|-------------|
| 1 Writings | Books, long essays, papers, newsletters | Core arguments that recur (3 or more times means a real belief), coined terms, reading lists | `01-writings.md` |
| 2 Conversations | Podcasts, long videos, AMAs, in-depth interviews | How the person answers under pressure, improvised analogies, moments of changed position, questions the person refuses | `02-conversations.md` |
| 3 Expression | X/Twitter, other social platforms, short posts | Frequent words and sentence patterns, controversial stances, humor, public debates | `03-expression-dna.md` |
| 4 Others | Analyses by others, reviews, criticism, biographies | Patterns that others see, criticism and controversy, comparison with peers | `04-external-views.md` |
| 5 Decisions | Major decisions, turning points, controversial actions | Context and logic of decisions, later reflection, cases where words and actions match or differ | `05-decisions.md` |
| 6 Timeline | The full timeline from birth or debut to now | Key milestones, turning points in thinking, activity in the last 12 months (to prevent staleness) | `06-timeline.md` |

#### Hard requirements for every agent

- Write the results to `references/research/0X-xxx.md`.
- Give the source and its reliability for each item (primary > secondary > inference).
- Separate "what the person said", "what others say about the person", and "what I infer".
- When you find a contradiction, keep it. Do not smooth it over.

#### Agent prompt template

When you start a subagent, give the task in this structure (Agent 1, writings, as the example):

```
Your task: research the books and long-form writing of [Name].

Search for:
- Books by this person (title, core argument, year)
- Long newsletters, blogs, papers
- Core arguments that appear 3 or more times (these are real beliefs)
- Coined terms and concepts
- Reading lists (they show the intellectual lineage)

Output:
- Write to [skill folder]/references/research/01-writings.md
- Give the source URL and reliability for each item
- Separate primary (written by the person) from secondary (summaries by others)
- Record contradictions as they are. Do not reconcile them.

Source rules: do not use content farms, unattributed quote sites, or
AI-generated summaries as sources.
```

For the other 5 agents, change the search targets and the output file name in the same structure.

#### Helper tools (when available)

- Books: use books the user owns or legally available text. Put them in `sources/books/`. Do not download pirated copies.
- Video subtitles (scripts included):
  - Step 1, download: `bash [skill folder]/scripts/download_subtitles.sh <YouTube_URL> [output folder]`. It prefers English manual subtitles, then any manual subtitles, then English auto-generated subtitles. It writes SRT or VTT files.
  - Step 2, clean up: `python3 [skill folder]/scripts/srt_to_transcript.py <input.srt> [output.txt]`. It removes timestamps, numbers, HTML tags and repeated lines, and writes a clean transcript. Save it in `sources/transcripts/`.
  - If the user gives a local video file with no subtitles, use an installed video-transcription skill or tool.
- Podcasts: search for transcript sites.
- Research summary (for Phase 1.5): `python3 [skill folder]/scripts/merge_research.py <skill folder>`. It scans `references/research/01-06`, counts sources and the share of primary and secondary sources, and lists key findings. It prints the Phase 1.5 table, so you do not count by hand.
- Quality check (for Phase 4): `python3 [skill folder]/scripts/quality_check.py <path to SKILL.md>`. It checks the content of the skill: models with evidence and limits, heuristics, filled style fields, specific honest boundaries, tensions, primary-source share, research files with URLs, and leftover placeholders. It prints PASS or FAIL for each item.

#### Use installed information skills

Before Phase 1, scan `.claude/skills/` for skills that help with research. If you find any, use them first. They are usually more stable than plain web search.

| Kind of installed skill | Use | When |
|-------------------------|-----|------|
| Video analysis or transcription | Extract a transcript from a local video | The user gave a video with no subtitles |
| Web article reader | Read the full text of a web page | You found an important article URL and need the exact text |
| Multi-platform fetcher | Get content from X, Reddit, YouTube and other platforms | You need platform content that web search does not reach |
| Structured research | Deep research on one dimension | One dimension needs depth, not breadth |
| PDF reader | Read PDF books and papers | The user gave PDF material |

When you start a subagent, tell it the names and uses of the available skills, so that it uses them during research. This works much better than leaving the agent to find its way with web search.

#### Source priority

| Source type | What it shows | Weight |
|-------------|---------------|--------|
| Primary material from the user | Full original text, no second-hand filter | Highest+ |
| The person's own writing | Systematic thinking | Highest |
| Long conversations and interviews | Improvised thinking | Highest |
| Records of real decisions | Real behavior against stated beliefs | Highest |
| Social media | Style, quick reactions | Medium |
| Views of others | Outside view, blind spots | Medium |
| Second-hand summaries | Reference only, check first | Low |

#### Excluded sources (always)

- Content farms and SEO pages that rewrite other articles.
- Quote sites with no original source. Many famous quotes online are fake.
- AI-generated summaries, unless you compare each claim with the original.
- Closed platforms where you cannot open or check the original.

For people outside the English-speaking world, prefer original-language primary sources and established national media. Use the same exclusion rules for platforms in that language.

#### Failure modes and fallbacks

Distillation is a long, multi-agent, online task. The first three rows below happened to real users. For each row, use the first fix. If it still fails, use the fallback.

| Trigger | First fix | Fallback |
|---------|-----------|----------|
| The runtime does not support parallel subagents or background tasks (some runtimes hang in Phase 1) | Run the 6 research tasks one after another. Save each file before you start the next. Never wait on a background notice. | One agent does 6 rounds of research, one dimension per round, and saves each round at once. |
| The context window is too small (a full run can pass 500k tokens, and a 200k model cannot finish it) | Run by phase. At the end of each phase, save the state to `references/research/`. A new session resumes from the files, which act as checkpoints. | Run a 200k model in 3 sessions: Phase 0-1, Phase 1.5-2.5, Phase 3-5. Each session first reads the saved files. |
| Cost runs out of control (the user did not expect the token use) | The tier choice in Phase 0A is the guard. Give the cost level and let the user choose before you start. | If the user stops midway, the saved research files are a usable partial result. The next run continues from them. |
| One agent times out (5 minutes of search with no useful result) | Do not wait. Continue, and mark "insufficient information" in Phase 2. | Say in the honest boundaries that this dimension is weak. |
| Web search is not available | Use an equivalent tool in the runtime (fetch, browser tools, an installed information skill). | Switch to local-material-only mode and ask the user for material. |
| Few sources (fewer than 10 usable) | Tell the user in Phase 0.5 and lower the expectations (2-3 mental models). | Expand the honest boundaries and mark the parts that are inference. |
| Agents disagree | Keep the contradiction. It is a useful signal. | Record it in the internal tensions section. |

Key rule: an honest 60-point skill with clear limits is better than a 90-point skill that looks perfect but is invented.

### Phase 1.5: Research review checkpoint

**CHECKPOINT. After all agents finish, pause and show a summary of research quality:**

```
┌──────────────────┬──────────┬────────────────────────────┐
│ Agent            │ Sources  │ Key findings               │
├──────────────────┼──────────┼────────────────────────────┤
│ 1 Writings       │ 8        │ Core arguments: ...        │
│ 2 Conversations  │ 5        │ Changed position after ... │
│ 3 Expression     │ 120 posts│ Frequent words: ...        │
│ 4 Others         │ 6        │ Main criticism: ...        │
│ 5 Decisions      │ 4        │ Key decisions: ...         │
│ 6 Timeline       │ complete │ Latest: ...                │
├──────────────────┼──────────┼────────────────────────────┤
│ Contradictions   │ 2        │ Agent 1 says X, Agent 4 Y  │
│ Thin dimensions  │ none     │                            │
└──────────────────┴──────────┴────────────────────────────┘
```

If the user approves the research quality, go to Phase 2.
If the user finds a dimension too thin, add research, then continue.

Why this checkpoint matters: research quality caps the quality of the final skill. Garbage in, garbage out. A fix here costs far less than a rework in Phase 4.

---

### Phase 2: Extract the framework (synthesis)

Combine the material from all agents and extract the framework. First read `references/extraction-framework.md` for the triple test of mental models (cross-domain recurrence, generative power, distinctiveness).

#### 2.1 Mental models (3-7)

Steps:

1. Scan. Read `01-writings.md` to `05-decisions.md` one by one. List every candidate idea: views the person repeats, coined terms, core claims. You usually get 15-30 candidates.
2. Apply the triple test to each candidate (details in `references/extraction-framework.md`):
   - Cross-domain recurrence: does it appear in 2 or more different fields or topics?
   - Generative power: does it predict the person's stance on new problems?
   - Distinctiveness: is it something that not every smart person thinks?
   - Passes all three → mental model. Passes one or two → demote to a decision heuristic. Passes none → drop it.
3. Rank and cut. Rank by distinctiveness, the most unique first. Keep the top 3-7. Fewer is better: 3 deep models beat 10 shallow principles.
4. Record each model with its name, a one-line description, evidence (2 or more contexts), how to apply it, and its limits.

#### 2.2 Decision heuristics (5-10)

These are the person's quick rules for judgment. Write them as "if X, then Y", each with a concrete case.

#### 2.3 Expression DNA

| Dimension | What to extract |
|-----------|-----------------|
| Sentence style | Long or short sentences, questions or statements, density of analogies |
| Vocabulary | Frequent words, coined terms, words the person avoids |
| Rhythm | Conclusion first or build-up first, how arguments turn |
| Humor | Sarcasm, self-mockery, absurdity, dry humor, or none |
| Certainty | "I am not sure" type or "obviously" type |
| Citation habits | Whom the person quotes, and what kind of source |

#### 2.4 Values and anti-patterns

- Values: the 3-5 core values, in order of priority.
- Anti-patterns: behaviors and ways of thinking that the person rejects outright.
- Tensions: internal conflicts between values. They are the source of depth.

#### 2.5 Intellectual lineage

Who influenced the person → who the person influenced → where the person sits on the map of ideas.

#### 2.6 Honest boundaries

Always write these limits:

- The skill cannot predict how the person reacts to a truly new problem.
- The skill cannot replace the person's creativity and intuition.
- Public statements and private thinking can differ.
- The information stops at the research date.

---

### Phase 2.5: Extraction checkpoint

**CHECKPOINT. After Phase 2, pause and show the extraction summary for approval:**

```
Extraction summary:
- Mental models: N (list the names)
- Decision heuristics: N
- Expression DNA: [3 key traits]
- Core tensions: N pairs
- Honest boundaries: N
```

If the user approves, go to Phase 3.
If the user thinks a model is wrong or missing, go back to Phase 2, adjust, then continue.

Why this checkpoint matters: extraction is the most subjective step. An approval here avoids writing a 400-line SKILL.md in the wrong direction.

---

### Phase 3: Build the skill

Assemble the Phase 2 results into a runnable SKILL.md.

#### Step 1: Read the template

Read `references/skill-template.md` for the standard structure. The template defines the full skeleton: frontmatter, response modes, answer workflow, identity card, mental models, decision heuristics, expression DNA, timeline, values, intellectual lineage, honest boundaries, and research sources.

#### Step 2: Fill in the content

Fill each template section with the Phase 2 results:

| Template section | Source |
|------------------|--------|
| Frontmatter description | Number of sources, number of models, triggers. Keep it near 300 characters and never over the loader limit of about 1,024 characters. Give one line on what the skill is. Add clear trigger phrases, such as "use X's lens". Add one line that says it does not trigger on general questions. Long tails of keywords break the limit, burn tokens in every session, and raise false triggers. The name and the coined concepts do the matching. |
| Response modes | Use the template's rules. Set the default mode from the purpose in Phase 0A. Keep both modes. |
| Answer workflow (agentic protocol) | Derive it from the mental models. See the guide below. |
| Identity card | Timeline (06) and writings (01). A 50-word self-introduction in the person's voice. |
| Mental models | Phase 2.1, each with name, evidence, application and limits. |
| Decision heuristics | Phase 2.2, each with a situation and a case. |
| Expression DNA | Phase 2.3, as style rules for role-play mode. |
| Timeline | Agent 6, cut down to a table of key points. |
| Values and anti-patterns | Phase 2.4. |
| Intellectual lineage | Phase 2.5. |
| Honest boundaries | Phase 2.6, plus the research date. |
| Research sources | Citations from all agents, split into primary and secondary. |
| Footer | Fixed text: `> Generated with Impersonator.` |

#### Guide: the answer workflow (agentic protocol)

Why this section is needed: it makes the persona act like the person, not only sound like the person. Without it, a person skill that faces a factual question invents an answer from training data. With it, the skill does its homework first, as the real person does. This step turns a parrot into a reliable thinking advisor.

Position: after the response modes, before any example dialogs.

Generation rules: the workflow has 3 steps. The research categories in Step 2 come from the distilled mental models. They are not a fixed template.

```markdown
## Answer Workflow (Agentic Protocol)

**Core rule: [Name] does not answer from feel. For a question that needs facts, research first, then answer.**

### Step 1: Classify the question

| Type | Signs | Action |
|------|-------|--------|
| Needs facts | A specific company, person, event, product or market | Research first (Step 2) |
| Pure framework | Values, ways of thinking, life advice | Answer from the mental models (Step 3) |
| Mixed | A concrete case used to discuss a general idea | Get the case facts, then apply the framework |

Rule: if missing current information makes the answer clearly worse, research first. One extra search beats an invented answer.

### Step 2: Research the way [Name] does

**Use tools (web search or equivalent) to get real information. Do not skip this step.**

[3-5 research categories derived from the person's mental models and analytic habits, each with 4-6 concrete things to look up]

#### Research output
After the research, keep a fact summary internal (do not show it to the user), then go to Step 3.
The user sees [Name]'s judgment based on real facts, not a research report.

### Step 3: Answer the way [Name] does

Use the facts from Step 2 (if any), the mental models and the active response mode.
```

How to derive the Step 2 research categories: use the mental models to find the first thing that the person looks at in a problem. Turn that into concrete search categories. Examples:

| Person | Core mental models | Research categories |
|--------|--------------------|---------------------|
| Munger | Multiple mental models, inversion, incentives | The moat, management incentives, the biggest risk (inversion), historical analogies |
| Feynman | First principles, doubt of authority | Basic physical or mathematical limits, logic gaps in official claims, the experimental data |
| Taleb | Antifragility, tail risk, the limits of expert knowledge | Extreme cases, who carries the tail risk, the track record of expert forecasts |
| MrBeast | Attention engineering, test and iterate | Competitor data (views, engagement), room for title and thumbnail tests, audience profile |

Hard limits:

- The research categories come from the mental models. A generic "search for related information" is not allowed.
- Each category gives concrete instructions (what to search, which data to read). Abstract descriptions are not allowed.
- Group the categories by question type (for Munger: companies, people, events), so that the user of the skill finds the right one fast.

#### Step 3: Self-check

After you build the skill, read the self-check list at the end of `references/extraction-framework.md` and check each item. Mark the items that fail and go back to the matching phase to fix them.

#### Step 4: Output

Write the finished SKILL.md to `.claude/skills/[person-name]-perspective/SKILL.md`.

---

### Phase 4: Test quality

After you generate the skill, run the static check, then three behavior tests in subagents. Use subagents so that the main agent does not grade its own work.

#### 4.0 Static check

Run `python3 [skill folder]/scripts/quality_check.py <path to SKILL.md>`. Fix every failed item in Phase 2 or 3. Never rename a heading only to pass a check.

#### 4.1 Known-stance test (sanity check)

Pick 3 questions on which the person has a public position. Start a subagent that answers with the new skill, and compare the answers with the real positions.

- Same direction → the models work.
- Different direction → go back and adjust the weight of the models.

#### 4.2 Edge test

Pick 1 related question that the person never discussed in public. Let the skill infer an answer.

- Expected result: "Based on models X and Y, the answer is probably ..., but this is uncertain."
- The skill must not answer with false certainty.

#### 4.3 Voice test

Let the skill write a 100-word analysis. Judge:

- Does it show the person's expression traits?
- Is it free of generic AI platitudes?
- Is it more than a collage of real quotes?

#### 4.4 Baseline test

Answer 3 of the test questions twice more: once with a plain "think like [Name]" prompt and no skill, and once with no persona. A blind judge compares the three answers. If the skill reasons more like the person than the plain prompt does, the skill earns its place. For very famous people, the plain prompt is often as good. Tell the user the result in all cases.

#### 4.5 Pass criteria

| Item | Pass | Fail signal |
|------|------|-------------|
| Number of mental models | 3-7, each with evidence | Fewer than 3 or more than 10 |
| Limits of each model | The failure conditions are written | Only strengths |
| Expression DNA | 100 words are enough to recognize the person | Reads like generic ChatGPT |
| Honest boundaries | At least 3 specific limits | Only "cannot replace the person" |
| Internal tensions | At least 2 pairs | Views that agree too neatly (fake) |
| Primary-source share | More than 50% | Mostly second-hand summaries |
| Baseline | The skill beats or matches the plain prompt | The skill is worse than the plain prompt |

If the skill passes, deliver it. If it fails, mark the weak points and go back to Phase 2.
Iteration limit: loop from Phase 2 to Phase 4 at most twice. If items still fail after 2 rounds, mark the weak dimensions in the honest boundaries and deliver the best current version. Do not polish forever.

**CHECKPOINT.** Show the test results. The task is complete only after the user approves them.

---

### Phase 5: Two-agent refinement (standard final step)

After Phase 4 passes, start a two-agent refinement to make the skill easier to act on.

Start two agents in parallel:

Agent A (skill optimizer view):

- Score the SKILL.md on 8 structural dimensions: workflow clarity, edge conditions, checkpoint design, specificity of instructions, and so on.
- Dry-run 3 typical test prompts and judge the results.
- Output: concrete fixes for the 2 weakest dimensions, with example replacement text.

Agent B (skill author view):

- Check that the activation triggers cover real use.
- Check that the response-mode rules are actionable (question routing, frequency limits, failure prevention).
- Find missing key information.
- Output: 2-3 concrete text changes, with example replacement text.

**CHECKPOINT. The main agent merges both reports, applies the changes that do not conflict, and shows a change summary for the user to approve.**

Refinement standard: every change must make the skill run correctly on activation. Do not only add content. The AI that loads the skill must know its first step and its stop points.

---

## Updating an existing skill

When the user says "update the X skill" or "X has news":

1. Read the existing SKILL.md. Find the research date in the honest boundaries section and note how old it is.
2. Start only Agent 2 (recent conversations), Agent 5 (recent decisions) and Agent 6 (timeline update).
3. Compare the new information with the existing content:
   - New information strengthens a model → add cases.
   - New information contradicts a model → mark the change and update the model.
   - A new thinking pattern appears → consider a new model.
4. Update the recent activity section and the research date.
5. Do not rewrite the whole skill. Update it in steps.

---

## Taste rules (quick reference)

If a judgment is hard, read this. The numeric standards are in the Phase 4 pass criteria.

| Rule | In one line |
|------|-------------|
| Long form over sound bites | A 3,000-word essay shows more of a person's thinking than 50 posts |
| Controversy over consensus | The most disputed views show the most uniqueness |
| Change over constancy | A changed position tells you more than a fixed one |

### Anti-pattern blacklist (never do these)

| # | Anti-pattern | Why, and what to do instead |
|---|--------------|-----------------------------|
| 1 | Inventing things the person never said | The web is full of fake quotes. Every quote needs a source. Drop a quote that you cannot trace. |
| 2 | Presenting common sense as the person's unique insight | Content that fails the distinctiveness test does not become a mental model. |
| 3 | Ignoring negative views and controversy | Agent 4's criticism protects against a fan filter. Too little criticism means the research failed. |
| 4 | Forcing a result with too little information | An honest 60-point skill beats an invented 90-point skill. |
| 5 | Using content farms, unattributed quote sites or unchecked AI summaries as sources | They rewrite, distort and cannot be checked. No exceptions. |
| 6 | Running the whole process in one session on a small-context model | Context overflows between Phase 1 and 2. Split the run as the fallback table says. |
| 7 | Starting without stating the cost level | A full distillation is a heavy task. The user has the right to choose a tier first. |
| 8 | Distilling a living private person without stating the limits | This touches privacy and consent. The user must supply the material and get the person's consent. |
| 9 | Generating a skill with no drift guard | In long chats, a persona skill loses its frame and falls back to a generic assistant voice. Keep the response-mode rules and the expression DNA complete. |
| 10 | Turning checkpoints into delivery blocks | A checkpoint lets the user correct the course. It does not hold output hostage. Give defaults wherever possible. |
| 11 | Gaming the quality check | Renaming headings to pass a check hides real gaps. Fix the content. |

---

## Special cases

### Living people and historical figures

- Living people: watch for staleness. State the cutoff date and suggest regular updates.
- Historical figures: the material is stable, but biographies can be biased. Cross-check several sources.

### Topic skills and person skills

When the input is a topic, not a name (for example "value investing", "product restraint", "antifragile decisions"), each phase changes:

| Phase | Person skill | Topic skill |
|-------|--------------|-------------|
| 0A | Settle the name and focus | Settle the topic boundary and the audience ("value investing": one school or all schools?) |
| 0.5 | `[person]-perspective/` | `[topic]-framework/`, same folder layout |
| 1 | 6 agents on one person | First find the 3-5 core people or schools of the topic, then give each person 1-2 agents instead of 6 |
| 2.1 | Extract one person's mental models | Extract the shared framework of the field (what all schools agree on) and the differences (A says X, B says Y) |
| 2.3 | Imitate one person's expression | Do not imitate a person. Use a neutral, professional voice. |
| 2.4 | One person's internal tensions | The basic disagreements between schools (for example value investing against growth investing) |
| 3 | Use skill-template.md | Adjust the template: remove role-play mode and the identity card, add a "framework overview" and a "school comparison" |
| 4 | Compare with the person's known positions | Compare with accepted classic cases in the field |

### Little-known people (very few public sources)

When the Phase 0.5 assessment finds fewer than 10 usable sources:

1. Tell the user in Phase 0.5: "This person has very little public information. The skill quality will be limited."
2. Cut the mental models to 2-3, and mark each one "inferred from limited information".
3. Expand the honest boundaries. List the dimensions with too little information.
4. If the user can give primary material (books, internal recordings, private messages), use it first.

### Distilling the user

When the user says "distill me" or "make a skill of me":

1. Impersonator cannot find the user's thinking framework in public sources. The user must supply material.
2. Ask for: personal articles or blogs, recorded videos or podcasts, decision memos, a self-description.
3. In Phase 1, the 6 agents analyze the user's material instead of searching the web.
4. Watch for self-perception bias. The user can overrate some traits and miss blind spots. Ask how people close to the user see them.

---

## Last words

Impersonator does not make people. It makes a mirror.

A good person skill lets you look at your own problem through another person's eyes. The point is not to imitate that person. The point is to widen your own thinking.
