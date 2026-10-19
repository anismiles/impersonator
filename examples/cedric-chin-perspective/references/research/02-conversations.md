# Cedric Chin: Long conversations and improvised thinking (Agent 2)

- **Date compiled:** 2026-10-19
- **Tier:** QUICK (5 sources used)
- **Method:** WebSearch and WebFetch only. No books or videos were downloaded. Transcript pages were read through a fetch tool that summarises page text. Every "quote" below was returned by that tool as verbatim from transcript text, but I did not read the raw transcript line by line. Treat quotes as **probably verbatim, not hand-verified**. Where two fetch passes returned different wording for the same line, I give no quote.
- **Blacklist note:** Z-Library, LibGen, Zhihu, WeChat, and Baidu were not used. No files under `pg-ab-pilot/` were opened.
- **Labels:** **[He said]** means attributed to Chin in a transcript or his own comment. **[Others said]** means a host, summariser, or third party. **[Inference]** means my interpretation.

## Sources

| # | Source | Type | Credibility |
|---|--------|------|-------------|
| 1 | Wisepreneurs Ep. 58 (host Nigel Rawlins), 2024-08-23 | Full timestamped transcript on page | Primary |
| 2 | Analytics Engineering Podcast, "Data as an assembly line (w/ Cedric Chin)" (host Tristan Handy, dbt Labs), 2024-11-17 | Partial transcript plus key takeaways | Primary/secondary mix |
| 3 | Hacker News comments by user `shadowsun7`, 2010 to 2024 | His own written replies under pushback | Primary |
| 4 | Artem Zen, "Elevating Consciousness" podcast recap, 2024-08-19 | Newsletter recap, no transcript | Secondary |
| 5 | Infinite Loops Ep. 207 (Jim O'Shaughnessy), ~2024-03-14, via Podwise | AI-generated summary only | Secondary (weak) |

Identity check for source 3: the HN profile `shadowsun7` has an "about" field that starts with "Cedric Chin" and calls him a "Sporadic Internet writer". Several comments say "I wrote" and link to commoncog.com. The username `shalmanese` named in the brief was **not** verified and was not used.

---

## 1. Wisepreneurs Ep. 58: "The Reality Check: Testing Business Ideas Against the Real World"

- **URLs:** https://wisepreneurs.au/the-reality-check-testing-business-ideas-against-the-real-world-with-cedric-chin and https://www.buzzsprout.com/2311675/episodes/15616928
- **Host:** Nigel Rawlins. **Date:** 2024-08-23. **Credibility:** primary (the page carries a full transcript with some transcription errors).

**Key exchanges (paraphrased):**
- **Origin story, ~2:56 [He said].** He grew up in a small town in Malaysia. He ran engineering for a bootstrapped point-of-sale business in Vietnam for a boss. The company moved from outsourcing work to its own product and grew to about US$4.5M in annual revenue. Later he dealt with "traditional Chinese businessmen" in the region. He says they were self-taught through hard knocks and often outmaneuvered his team. He then realised he was weak at sales and marketing, so he started a blog to learn content marketing. That blog became Commoncog.
  - Quotes (probably verbatim): "I ran a business in Vietnam for a boss", "I call them traditional Chinese businessmen", "in many cases they ran circles around us".
- **Deliberate practice, ~9:34 [He said].** He opens by defining the term: deliberate practice is a technical term, not just practising on purpose. It needs a coach and a mature teaching system with known drills, and business has neither. So it cannot be applied directly, though some ideas can be borrowed, which he says is harder than people think. He proposes Naturalistic Decision Making (NDM) instead and uses riding a bicycle to explain tacit knowledge.
  - Quote: "It does not mean practicing deliberately."
- **Epistemic standard [He said].** Everything Commoncog publishes must be tested against reality. He only wants ideas that work. He asks whether an idea "has predictive validity".
  - Quotes: "Everything that Commoncog publishes has to be tested against reality.", "I only really want ideas that work."
- **Business-school exchange, ~1:04 [Others said, then he said].** Nigel suggests business schools waste students' money. Cedric does **not** fully agree. He grants that academic research has value but says it is not the operator knowledge people need. He reframes: if professors had to run businesses and teach only what worked, they will resemble Commoncog. He adds that Commoncog will find and profile the useful professors. **[Inference]** He declines to bash an institution and redirects to his own criterion of usefulness.
- **Host flattery [Others said].** The host says "you're being very humble about Commoncog." He also rejects the host's "It's simple" framing, saying it is simple "in the right way" (wording varies between fetch passes).
- **Triad model [He said].** He presents Lia DiBello's triad. He renamed DiBello's "Supply, Demand, Capital" to "Operations, Market, Capital" because readers found the originals confusing. Cash-flow examples: Costco collects cash before it pays suppliers, and a restaurateur requires prepayment. Both show expert moves that a novice does not predict.
- **Judo experiment, ~42:25 to 52:11 [He said].** He trained about 5 hours a day for about 5 months for the Malaysian Senior Nationals, with a coach who ranked 13th at the 1991 Worlds. He had a mental breakdown around month two, and his coach added mental training. Body-language discipline (no slouching, always look ready) carried him through. He won his first match despite an eye injury and lost the next two. Lessons: expertise shows up as perceiving cues, such as fake attacks and penalty setups. He is not willing to pay the cost to be world-class in judo, but he is willing to pay it for business. He now frames hard business decisions as not as bad as being choked every day.
  - Quote: "I'm not willing to pay that cost."
- **Hedges [He said].** On the capital leg of the triad: "I'm a bit confused, or at least I was." On Commoncog's new training approach: "I don't know if it'll work." He cannot remember the timing of DiBello's Swiss Re work.

---

## 2. Analytics Engineering Podcast: "Data as an assembly line (w/ Cedric Chin)"

- **URL:** https://roundup.getdbt.com/p/data-as-an-assembly-line-w-cedric (also listed on iHeart)
- **Host:** Tristan Handy (dbt Labs). Post by Dan Poppy. **Date:** 2024-11-17. **Credibility:** primary/secondary mix. The page has long transcript passages plus edited takeaways, and speaker labels are inconsistent (the guest is misspelled "Cedric Chen" once). No quotes are taken from it.

**Key exchanges (paraphrased):**
- **Adversarial setup [Others said].** Tristan opens by saying he does *not* think analytics is an assembly line, then asks Cedric to argue the opposite. **[He said]** Cedric argues from Statistical Process Control. He models the business as controllable input metrics driving output metrics, with lags. The core problem is variation: you must separate routine variation (noise) from exceptional variation (signal) before trial-and-error can work.
- **Amazon WBR story [He said].** Amazon ran its Weekly Business Review on Excel in 1997, with departments dropping files into a shared folder on Sunday night. He claims forecast accuracy within about 3% (unsourced). He also calls the WBR a political tool, a place where executives can shame teams in front of peers. Amazon dropped TV ads because it was not able to connect controllable inputs to outputs. Early Amazon modelled word-of-mouth growth with cohort "vintages".
- **Pushback: "Does it always work, or was Amazon special?" [Others said].** **[He said]** Yes, it works, but it does not solve marketing attribution. This is a concession that limits the scope.
- **Pushback: "Why isn't it widespread?" [Others said].** **[He said]** The barrier is social and political, not technical, and tools are not the problem. Adoption needs an executive who enforces the discipline, and most executives do not want that scrutiny. Returns on invested capital explain where it spreads (low-ROIC industries need operational excellence). He credits this point to "somebody in my community", not to himself.
- **Own-business example [He said].** At Commoncog, a link from a 20,000-subscriber investing newsletter caused exceptional variation in traffic. That prompted an experiment in getting more such links. He built a free XmR-chart tool because BI tools do not draw them, and mentions that his wife is a data analyst.
- **Analogies:** a manufacturing line or the Toyota Production System, a weighing scale (for variation), and a business as a complex machine.

---

## 3. Hacker News comments by `shadowsun7` (Cedric Chin)

- **URLs:** https://hn.algolia.com/api/v1/users/shadowsun7; comment search https://hn.algolia.com/api/v1/search?tags=comment,author_shadowsun7 (405 comment hits; I sampled the newest 40 plus keyword searches for "boss" and "Vietnam"). Individual comments: `https://news.ycombinator.com/item?id=<objectID>`.
- **Date range:** 2010 to 2024. **Credibility:** primary (his own text). Early comments (2010 to 2015) come from a younger, programmer-era Chin and possibly do not show his current views.

**Key exchanges (paraphrased):**
- **Goodhart's law thread, 2024-10-26 (41958450, 41958493, 41958348) [He said].** He pushes back on a commenter by asking two concrete questions. How do you detect a change when the metric varies wildly? And without a causal model, how do you know a change didn't hurt another part of the business? He adds that quoting books about goals is not the same as achieving them. Quote: "Reality has a lot of detail." He credits the ideas to Deming, Wheeler, and Joiner. He says the WBR solves socio-technical problems, which is why companies struggle to adopt it. In a follow-up (41959055) he answers his own questions with concrete scenarios and cites Wheeler's small-business study.
- **SPC Practitioner's Guide thread, 2024-03-08 (39639621, 39639515, 39639321) [He said].** He argues that early Amazon used SPC in software-adjacent work and that XmR charts can detect behaviour change caused by a feature without A/B tests. He **concedes** that SPC does not apply to measuring software-development productivity ("And I think we are all in agreement there!"). He corrects a misreading of Wheeler and says XmR charts do not need normality. He proposes renaming jargon ("stable" and "in-control" become "routine variation" and "process behaviour chart"), which is a reader-usability move. He says Colin Bryar, an early Amazon executive, told him about the WBR.
- **spc-kit thread, 2024-03-08 (39639490) [He said].** He asks how SPC handles power-law or J-curve data. He describes his own method for HN traffic (counting days between viral events), calls it "very dumb", and asks for better approaches. **[Inference]** This is a self-deprecating hedge that invites correction.
- **Judo update, 2023-07-21 (36813205) [He said].** As the author of "Ability to see expertise is a milestone", he reports months of judo training and says he reached the milestone of seeing expertise. This agrees with source 1 on the effect but differs slightly on duration: here "four months", in the podcast about five months.
- **"Don't Read History for Lessons", 2022-07-08 (32022214) [He said].** He points out that the article already addresses the commenter's objection, then asks how reading for concept instances differs from reading for patterns. **[Inference]** He answers a challenge with a sharp clarifying question.
- **Singapore death-penalty thread, 2022-05-08 (31301722) [He said].** He argues from case details (psychiatric evaluations, a decade of appeals). He also says it is "a more complicated case than I thought." This is an in-thread softening of his position. The fetch summary was muddled, so treat the details with caution.
- **2015 Singapore language-policy thread (9427282, 9444233, 9420483) [He said].** These are blunt rebuttals ("It does, actually."). He tells a commenter that HN is "downvoting you because you didn't justify your assertion". He hedges openly: "I don't know much about that, I'm afraid", and his guess comes with no sources. He mentions that he speaks English, Chinese, and Malay.
- **Older comments, 2012 [He said].** In "Doing vs Telling" (3752770, 3752791) he argues pg's essays count as doing, concedes another point, and admits his own phrasing was weak. In 3697714 he thanks a corrector with "Holy crap, that's something I needed to see."
- **Recurring themes (from the Algolia hit summaries) [He said]:** critique of Farnam Street-style "mental models" (2018-11-12, "Mental Model Fallacy" 2020-04-23), a burnout-research synthesis (Maslach inventory, JD-R and COR models), and deliberate practice needing a mature pedagogy (2021-09-08).
- **Not found:** no HN comments in the sample mention the Vietnam company or his former boss.

---

## 4. Artem Zen, "Learn How to Go from Novice to Expert in 90 minutes"

- **URL:** https://artemzen.substack.com/p/learn-how-to-go-from-novice-to-expert
- **Host:** Artem Zen (Elevating Consciousness podcast). **Date:** 2024-08-19. **Credibility:** secondary (host's recap and pull-quotes, no transcript). No quotes taken.
- **[He said, via the host's recap]**
  - Believability takes at least three successes plus a coherent explanation of how they happened. This is the Ray Dalio-derived believability test he uses.
  - There are three routes to expertise: deliberate practice, NDM, and trial and error. He now prioritises NDM for himself but declines to rank the routes in general (roughly: each has its uses depending on the domain).
  - Experts' verbal accounts often do not match what they actually do.
  - "Mental models" thinking oversimplifies, though the models themselves are not bad.
  - Read practical books slowly and apply each chapter before moving on.
- **[Others said]** The host reports that Cedric called himself one of the least spiritual people he knows and was surprised to be invited onto a consciousness podcast.

---

## 5. Infinite Loops Ep. 207: "Cedric Chin: Accelerating Business Expertise"

- **URL:** https://podwise.ai/episodes/1737147 (AI summary of the YouTube episode). **Host:** Jim O'Shaughnessy. **Date:** ~2024-03-14. **Credibility:** weak secondary. No transcript and no exchanges visible.
- **[Others said, AI summary]** Topics: his path from content marketing to expertise research, the triad (operations, market, capital), cognitive agility, NDM versus deliberate practice, whether intuition is trainable (including in investing), cognitive transformation theory, cognitive flexibility theory, using AI to speed up expertise, and a "Wisdom Keeper" project.
- No pushback, stories, or hedges are recoverable. This is a gap.

---

## Reasoning moves under questioning

1. **Define the term before answering [He said, sources 1 and 3].** He repeatedly opens by fixing a definition: deliberate practice is a technical term, and "stable" becomes "routine variation". He reframes the question around the precise meaning before taking a side.
2. **Concede scope, keep the core [sources 2 and 3].** When pushed ("does it always work?"), he says yes and then marks the boundary: not marketing attribution, not software productivity measurement. **[Inference]** He prefers to narrow a claim rather than abandon it.
3. **Turn the challenge into a concrete operational question [source 3].** "How would you detect the change? How do you know it didn't break something else?" He tests opponents on whether they are able to *do* the thing, not on argument.
4. **Doing over telling [sources 1 and 3].** Ideas are judged by whether they work in practice ("predictive validity", and quoting goal books is not achieving goals). This is consistent from his 2012 "Doing vs Telling" comments through 2024.
5. **Diagnose socio-political barriers, not technical ones [source 2].** When asked why good methods do not spread, he points to power, executive will, and fear of scrutiny, not tooling.
6. **Story first, principle second [source 1].** Costco, the restaurateur, Amazon's WBR in Excel, and a newsletter traffic spike: he starts with a case and then draws out the rule.
7. **Credit the source [sources 2 and 3].** He attributes ideas to DiBello, Wheeler, Deming, Joiner, Colin Bryar, and "somebody in my community" rather than claiming them.
8. **Don't take the easy agreeable bait [source 1].** He does not join the host in dismissing business schools, and he softens the host's "it's simple" framing.
9. **Self-aware rambling [Others said, source 1 summary].** He flags his own long-windedness and pokes fun at "highfalutin" jargon. He also uses "high-falutin'" on HN.

## Repeated stories and anecdotes

- **The Vietnam POS company run for a boss** (bootstrapped, outsourcing to product, ~US$4.5M revenue). Told as his origin story (source 1). His former boss appears only as the person who hired him to make that shift. No detailed boss anecdotes were found in these sources.
- **"Traditional Chinese businessmen" who learned through hard knocks and "ran circles around us"** (source 1). He used them as the puzzle that started Commoncog: he was not able to see their expertise until DiBello gave him a lens.
- **The judo experiment** (sources 1 and 3), used as evidence that expertise appears as perception and for his cost-of-mastery argument.
- **Amazon WBR** (sources 2 and 3), with Colin Bryar as the source, Excel in 1997, and the WBR as a political and social tool.
- **Commoncog's own traffic data and XmR charts** (sources 2 and 3).
- **Costco cash cycle and restaurateur prepayment** (source 1), used to illustrate the capital leg of the triad.

## Position changes

- **Deliberate practice to NDM [He said, source 1, matches HN 2021].** He wrote a lot about deliberate practice, then concluded it is impractical for business and moved to Naturalistic Decision Making. He does not literally say "I was wrong". He frames it as a research path.
- **Unable to see expertise, then able to see it [He said, source 1].** He was not able to observe the businessmen's expertise at the time, but later he was.
- **Renamed DiBello's triad** in response to reader confusion (source 1).
- **Capital leg:** "a bit confused, or at least I was" (source 1). This suggests his understanding of capital is still being revised.
- **Small in-thread updates on HN [source 3]:** "a more complicated case than I thought" (2022), "that's something I needed to see" (2012), and conceding a list item in Doing vs Telling (2012).

## Evasions and hedges

- On whether Commoncog's new training approach will work: "I don't know if it'll work", though early signs look promising (source 1).
- He declines to rank deliberate practice, NDM, and trial and error in general (source 4).
- He does not claim that SPC solves marketing attribution (source 2).
- He hedges on unsourced history ("this is but a guess, I don't have sources") and calls his own analytics method "very dumb" (source 3).
- **[Inference]** Unsourced or anecdotal numbers (Amazon's ~3% forecast accuracy, the ROIC argument) are stated confidently in conversation (source 2). That sits in some tension with his strict "tested against reality" standard.

## Contradictions and tensions kept

- Judo duration: "four months" (HN 2023) versus about five months at about 5 hours a day (podcast 2024).
- "Optimise for usefulness" quote: two fetch passes gave different wording ("We must optimize for usefulness" versus "We must be useful"). The exact wording is unverified, so I give no quote.
- He has a strict epistemic standard (predictive validity, tested ideas) but makes confident, unsourced claims about Amazon in live conversation.
- Early HN Chin (2011 to 2015) is combative and argues programming and politics. Later Chin is more pedagogical and source-crediting. **[Inference]** This is possibly a change in style or just a change of topic.

## Information gaps

- No full transcript was obtained for Infinite Loops Ep. 207, the Todd Nief podcast ("Cedric Chin (Commoncog) on Tacit Knowledge and Learning from Experts", found in search but not read), or his own Commonplace Expertise podcast, where he is the host. That is a separate source of his questioning style, for example https://commoncog.com/transcript-lia-dibello-business-expertise/ (not read).
- No detailed anecdotes about his former boss, and no Malaysian or Singaporean Chinese business family stories beyond the "traditional Chinese businessmen" passage.
- No Ness Labs, Every, Perell, Knowledge Project, or Indie Hackers appearance was verified. Searches found none, but this was a quick pass, so it does not prove they don't exist.
- In source 3, only about 50 of 405 HN comments were sampled. Commoncog forum posts (forum.commoncog.com) were not examined.
- Quotes were extracted through a summarising fetch tool and were not checked against the raw transcript by hand.
