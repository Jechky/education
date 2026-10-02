# Context rot: measurable quality loss in LLMs and agents as context grows (thresholds in tokens, focus on Claude)

Research date: 2026-10-02. Legend: **[M]** = measured evidence (benchmark/paper), **[V]** = vendor statement (Anthropic or other model provider), **[O]** = opinion, practice note or secondary summary, **[Calc]** = my own calculation from cited inputs. Model generations are named for every number because many key studies predate the current Claude 4.6–5.5 generation.

## Q1: What did Chroma's "Context Rot" study (2025) measure, and where did performance drop?

### Takeaway
Chroma (July 2025) tested 18 frontier models, including 5 Claude models up to Opus 4 and Sonnet 4. Performance fell steadily and non-uniformly as input length grew, even on trivially simple tasks. The study names no single cliff in tokens. The drop is steeper when the question shares few words with the answer (low lexical overlap), when distractors are present, and when the text is coherent rather than shuffled. The clearest number comes from LongMemEval, which compares a focused ~300-token input with a full ~113K-token input: all models did much better on the focused version, and Claude showed the largest gap.

### Cited Findings
- **[M]** Publication: "Context Rot: How Increasing Input Tokens Impacts LLM Performance", July 14, 2025, by Kelly Hong, Anton Troynikov and Jeff Huber (Chroma). — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** 18 models tested. Anthropic: Claude Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5, Haiku 3.5. OpenAI: o3, GPT-4.1 (plus mini and nano), GPT-4o, GPT-4 Turbo, GPT-3.5 Turbo. Google: Gemini 2.5 Pro, 2.5 Flash, 2.0 Flash. Alibaba: Qwen3-235B-A22B, Qwen3-32B, Qwen3-8B. — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** Experiments run:
  - Needle–question similarity, scored by cosine similarity across 5 embedding models
  - Distractors (0, 1 or 4 topically related distractors)
  - Needle–haystack similarity
  - Haystack structure (coherent vs. randomly shuffled sentences)
  - LongMemEval (focused ~300 tokens vs. full ~113K tokens)
  - Repeated-words copying task (25 to 10,000 words)
  - NIAH variants used "8 input lengths" and "11 needle positions".
  — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** Needles with low similarity to the question degrade "more quickly in input length". Needles with high similarity stay stable for longer. — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** A single distractor already lowers performance compared with no distractors. Hallucinations caused by distractors increase with context length. — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** All 18 models did better on shuffled haystacks than on logically structured ones. This is counter-intuitive and suggests that coherent, realistic text (such as source code or a paper) is not easier for the model. — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** LongMemEval: every model family scored "significantly higher" on focused prompts (~300 tokens) than on full prompts (~113K tokens). Claude models showed the "most pronounced gap between focused and full prompt performance". — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** Repeated-words task: performance "consistently degrades" as length grows, and accuracy is highest when the unique word sits near the start. — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M]** Claude-specific behaviour:
  - Lowest hallucination rates of all tested models; Sonnet 4 and Opus 4 "tend to abstain when uncertain".
  - Opus 4 had a 2.89% refusal rate on the repeated-words task, partly citing copyright risk.
  - So some of the measured Claude "failures" are abstentions, not wrong answers.
  — [Chroma Research](https://www.trychroma.com/research/context-rot)
- **[M/O]** Caveats stated by the authors: the tasks are simpler than real use ("long context applications are often far more complex, requiring synthesis or multi-step reasoning"), and the study does not explain the mechanism behind the degradation. — [Chroma Research](https://www.trychroma.com/research/context-rot)

### Inferences
- The worst Claude result (focused vs. full LongMemEval) is closest to how agents actually work: a long, mostly irrelevant history with a little relevant content. For agents, this is a stronger argument for curating context than the NIAH curves are.
- Chroma sells retrieval/vector-database infrastructure, so it has a commercial interest in "don't stuff the context". The measurements are open and reproducible, but the framing should be read with that in mind.
- The tested Claude models (Sonnet 3.5 to Opus 4, 2024–mid-2025) are 2–4 generations older than current models (Opus 4.6+, Sonnet 4.6+, Opus 5/5.5). The absolute curves probably do not carry over, but the qualitative effects probably do (distractors, low-overlap queries, coherent text being harder).

### Gaps
- The fetched summary did not give per-model accuracy at specific token counts (for example "Claude Sonnet 4 at 32K = X%"). The figures exist in the report, but no reliable per-token numbers could be extracted.
- No Chroma re-run on Claude 4.5/4.6/5.x was found.

## Q2: Effective vs. advertised context in long-context benchmarks (Lost in the Middle, NoLiMa, RULER, Michelangelo, LongBench v2, Fiction.LiveBench)

### Takeaway
When a task requires more than literal string matching, the effective context of 2024–2025 models is far below the advertised context:
- **NoLiMa:** effective length is 1K–16K tokens for most models; Claude 3.5 Sonnet's effective length is 4K.
- **RULER:** effective length is 32K–64K for many 128K-claimed models, and above 128K only for the best (Gemini 1.5 Pro, Jamba 1.5, Qwen3-235B).
- **Michelangelo:** a sharp early drop at short context, then a plateau or linear decline.

Retrieval-style benchmarks such as MRCR now show large gains for Claude 4.6 (93% at 256K, 76% at 1M). Reasoning-heavy benchmarks lag behind.

### Cited Findings
- **[M] Lost in the Middle** (Liu et al., TACL 2023/2024; older models such as GPT-3.5-Turbo):
  - Performance is U-shaped: highest when relevant information is at the beginning or end of the input, and "significantly degrades" in the middle.
  - Contexts were only ~2K–6K tokens: 10/20/30-document QA, and key-value retrieval with 75/140/300 pairs.
  - For GPT-3.5-Turbo, multi-document QA with the answer in the middle fell to about the closed-book level (~56.1%).
  — [arXiv 2307.03172](https://arxiv.org/abs/2307.03172)
- **[M] NoLiMa** (Modarressi et al., Adobe/LMU, ICML 2025):
  - 13 models claiming at least 128K context, using needles with minimal lexical overlap with the question.
  - At 32K tokens, 11 of the 13 dropped below 50% of their short-context baseline.
  — [arXiv 2502.05167](https://arxiv.org/abs/2502.05167)
- **[M] NoLiMa effective length** = the longest context at which a model keeps at least 85% of its base score (base = accuracy at 250–1K tokens). Selected rows from [NoLiMa GitHub](https://github.com/adobe-research/NoLiMa):

  | Model | Claimed | Effective | Base | 1K | 4K | 8K | 16K | 32K |
  |---|---|---|---|---|---|---|---|---|
  | GPT-4.1 | 1M | **16K** | 97.0 | 95.6 | 91.7 | 87.5 | 84.9 | 79.8 |
  | GPT-4o | 128K | **8K** | 99.3 | 98.1 | 95.7 | 89.2 | 81.6 | 69.7 |
  | Claude 3.5 Sonnet | 200K | **4K** | 87.6 | 85.4 | 77.6 | 61.7 | 45.7 | 29.8 |
  | Gemini 2.0 Flash | 1M | **4K** | 89.4 | 87.7 | 77.9 | 64.7 | 48.2 | 41.0 |
  | Gemini 1.5 Pro | 2M | **2K** | 92.6 | 86.4 | 75.4 | 63.9 | 55.5 | 48.2 |
  | Gemini 2.5 Flash (no thinking) | 1M | **2K** | 94.4 | 90.1 | 79.4 | 68.2 | 57.9 | 48.4 |
  | Llama 3.3 70B | 128K | **2K** | 97.3 | 94.2 | 81.5 | 72.1 | 59.5 | 42.7 |
  | Llama 3.1 405B | 128K | **2K** | 94.7 | 89.0 | 74.5 | 60.1 | 48.4 | 38.0 |

- **[M] RULER** (NVIDIA, 2024; synthetic tasks beyond vanilla NIAH):
  - "Effective length" = the longest length at which the score still exceeds Llama2-7B's score at 4K (85.6%).
  - Examples:
    - GPT-4-1106: claimed 128K, effective 64K (96.6 at 4K, 93.2 at 32K, 87.0 at 64K, 81.2 at 128K).
    - Llama3.1-70B: 128K, effective 64K (66.6 at 128K).
    - Qwen2-72B: 128K, effective 32K (79.8 at 64K, 53.7 at 128K).
    - Gemini-1.5-pro: 1M, effective >128K (94.4 at 128K).
    - Jamba-1.5-large: >128K (95.1 at 128K).
    - Qwen3-235B: >128K (90.6 at 128K).
  - Quote: "despite achieving nearly perfect performance on the vanilla needle-in-a-haystack test, most models exhibit large degradation on tasks in RULER as sequence length increases."
  — [NVIDIA/RULER GitHub](https://github.com/NVIDIA/RULER)
- **[M] Michelangelo** (Vodrahalli et al., Google DeepMind, Sept 2024; Claude 3 Haiku/Sonnet/Opus and Claude 3.5 Sonnet included):
  - Tasks: Latent List, MRCR, IDK. Up to 128K tokens (Gemini 1.5 up to 1M).
  - Common trend: "one initial sharp super-linear drop in performance in short-context ... after which performance often either flattens out or continues to degrade at a roughly linear rate."
  - Claude 3.5 Sonnet was best on IDK. Claude models had "high refusal rates" on Latent List and were excluded from those plots.
  — [arXiv 2409.12640](https://arxiv.org/html/2409.12640v2)
  - A secondary summary calls this a "32K cliff" (most models degrade sharply before 32K, while Gemini 1.5 stays flat up to 1M). I could not verify this exact wording in the primary text. — [alphaxiv summary via search](https://www.alphaxiv.org/abs/2409.12640)
- **[M] LongBench v2** (THUDM, ACL 2025):
  - Human experts score only 53.7% under a 15-minute limit.
  - The best model answering directly scored 50.1%; o1-preview, with longer reasoning, scored 57.7%.
  — [arXiv 2412.15204](https://arxiv.org/abs/2412.15204), [LongBench v2 site](https://longbench2.github.io/)
  - A secondary compilation reports that Gemini 2.5 Pro led at 63.3%, while Claude 3.5 Sonnet scored 41.0% (vendor-reported). — [Superlinear Academy / yage.ai, Mar 2026](https://yage.ai/share/long-context-benchmark-en-20260315.html)
- **[M] Fiction.LiveBench** tests understanding of long serialized stories: theory of mind, chronology and inference, not plain retrieval. It added contexts up to 192K in its April 2026 update. — [Epoch AI description](https://epoch.ai/benchmarks/fictionlivebench), [fiction.live](https://fiction.live/stories/Fiction-liveBench-Feb-21-2025/oQdzQvKHw8JyXbN87)
  - Aggregators only report the 16K score, and they conflict for the same model. Claude 3.7 Sonnet is listed as 53.1 by [benchmarklist.com](https://benchmarklist.com/benchmarks/fiction_livebench/), as 83.3 by another source in search results, and as 50.0% by [llmlearner.com](https://llmlearner.com/rankings/fiction-livebench). Claude Opus 4.5 is listed as 37.5 (16K) by [benchmarklist.com](https://benchmarklist.com/benchmarks/fiction_livebench/). Treat these numbers as unreliable.
- **[M] MRCR v2, 8-needle** (newer Claude models):
  - At 1M tokens: Opus 4.6 scores 76%, Sonnet 4.5 scores 18.5%. — [Anthropic, Claude Opus 4.6 announcement, Feb 5, 2026](https://www.anthropic.com/news/claude-opus-4-6)
  - Secondary compilation of system-card numbers:
    - 256K: Opus 4.6 93.0%, Sonnet 4.6 90.3%, GPT-5.2 70.0%.
    - 1M: Opus 4.6 76.0%, Sonnet 4.6 65.8%, GPT-5.4 36.6%, Gemini 3 Pro 24.5% (third-party), Gemini 2.5 Pro 16.4%.
    - GraphWalks at 1M: Opus 4.6 71.1% (Parents task), about 40% (BFS).
    — [yage.ai compilation, Mar 15, 2026](https://yage.ai/share/long-context-benchmark-en-20260315.html)
  - A search snippet from the Opus 4.6 system card gives GraphWalks BFS 1M F1 = 38.7. — [Opus 4.6 System Card PDF](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf)
- **[O]** The same compilation claims that "a model's effective context capacity is typically only 60–70% of its nominal value", and that developers report Gemini 3 Pro degrading after using 15–20% of its window. Both are unsourced or anecdotal. — [yage.ai](https://yage.ai/share/long-context-benchmark-en-20260315.html)

### Inferences
- The benchmark families disagree because they measure different things:
  - Literal retrieval (vanilla NIAH, partly RULER, MRCR) looks good up to 128K–1M on modern models.
  - Latent or associative retrieval (NoLiMa) degrades from about 4K–16K on 2024–25 models.
  - Reasoning and synthesis (LongBench v2, Fiction.LiveBench, Michelangelo Latent List) is hard even at modest lengths.
  - Coding/document agents mostly need the latter two kinds of capability.
- For pre-2025 Claude (3.5 Sonnet), the measured evidence puts the "quality starts slipping" point at roughly 4K–8K tokens for non-literal recall (NoLiMa), with less than half the base score by 32K.
- For Claude 4.6+, retrieval at 256K is near-solved (90%+ MRCR). There is no comparable independent NoLiMa-style or reasoning-style curve, so it remains open how far the improvement carries over to multi-hop use of the context.

### Gaps
- No primary per-length Fiction.LiveBench numbers for Claude 4.x/5.x could be retrieved; the page is JavaScript-rendered and aggregators only show 16K.
- NoLiMa has no published rows for Claude 3.7/4.x/4.5+ in the fetched table.
- RULER rows for Claude models were not in the fetched table.
- No Claude 5/5.5 long-context numbers (MRCR, GraphWalks) were retrieved from the Opus 5 system card ([PDF link](https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf), not parsed).

## Q3: Claude long-context and agentic behaviour (Anthropic statements, model cards, independent evals)

### Takeaway
Anthropic's own documentation treats context rot as real: "As token count grows, accuracy and recall degrade". It recommends curating the context and using compaction rather than filling the window. Current Claude models (Opus 4.6+, Sonnet 4.6+, the 5.x line) have 1M-token windows. The strongest independent agentic measurement for Claude is LOCA-bench on Claude Opus 4.5. Accuracy was:

| Context | Accuracy |
|---|---|
| 8K | 96% |
| 16K–32K | 84% |
| 64K | 65% |
| 96K | 45% |
| 128K | 34% |
| 256K | 15% |

This is a much earlier and steeper decline than retrieval benchmarks suggest.

### Cited Findings
- **[V]** Anthropic docs: "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as *context rot*. This makes curating what's in context just as important as how much space is available." — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **[V]** Window sizes:
  - 1M tokens (the default, at standard pricing): Opus 4.6, 4.7, 4.8, 5, 5.5; Sonnet 4.6, 5, 5.5; Fable/Mythos 5.x.
  - 200K tokens: Sonnet 4.5 and other older models.
  - Everything counts toward the window: system prompt, tool definitions, tool results, images and thinking.
  — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **[V]** On Opus 4.5 and later and Sonnet 4.6 and later, earlier thinking blocks are kept by default and count as input tokens. On earlier models they are stripped automatically. This makes context grow faster in agent loops on newer models. — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **[V]** "Context awareness":
  - Sonnet 5, Sonnet 4.6, Sonnet 4.5 and Haiku 4.5 receive a `<budget:token_budget>` tag and a `Token usage: X/Y; Z remaining` warning after each tool call. Image tokens are included.
  - Opus 4.7 and later Opus models and Sonnet 5.5 do not receive these tags; "task budgets" (beta) replace them.
  — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **[V]** Server-side compaction (beta, Claude 4.6+) is described as "the primary strategy" for long-running agentic workflows. Context editing adds tool-result clearing and thinking-block clearing. — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- **[V]** Anthropic engineering blog "Effective context engineering for AI agents" (Sept 29, 2025):
  - Describes an "attention budget" and "n² pairwise relationships for n tokens".
  - Goal: "the smallest possible set of high-signal tokens".
  - Claude Code compaction summarizes the history and continues "with this compressed context plus the five most recently accessed files".
  - Tool-result clearing is called "one of the safest lightest touch forms of compaction".
  - Sub-agents "return only a condensed, distilled summary of its work (often 1,000–2,000 tokens)".
  — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **[V]** Anthropic "Effective harnesses for long-running agents" (Nov 26, 2025):
  - "Compaction isn't sufficient" for multi-window projects, even with Opus 4.5.
  - Recommends an initializer agent and coding agent, a `claude-progress.txt` file, a JSON feature list (200+ features in the example) and git commits as the handoff state.
  - Documented failure modes: trying to one-shot the task and running out of context mid-feature; later sessions declaring the project done too early.
  — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **[V]** Opus 4.6 announcement (Feb 5, 2026):
  - "A common complaint about AI models is 'context rot,' where performance degrades as conversations exceed a certain number of tokens."
  - MRCR v2 8-needle at 1M: Opus 4.6 76%, Sonnet 4.5 18.5%.
  - Introduced context compaction at "a configurable threshold".
  — [Anthropic news](https://www.anthropic.com/news/claude-opus-4-6)
- **[V]** Opus 4.7 announcement (Apr 16, 2026):
  - New tokenizer: the same text maps to roughly "1.0–1.35×" as many tokens.
  - Partners report "more consistent long-context performance"; no MRCR or GraphWalks numbers were given.
  - Improved "file system-based memory" across multi-session work.
  — [Anthropic news](https://www.anthropic.com/news/claude-opus-4-7)
- **[M] LOCA-bench** (Zeng, Huang, He; HKUST; Feb 2026):
  - Measures agents under controlled context growth: the environment-description length is scaled from 8K to 256K tokens.
  - Claude Opus 4.5 accuracy:

    | Environment context | 8K | 16K | 32K | 64K | 96K | 128K | 256K |
    |---|---|---|---|---|---|---|---|
    | Accuracy | 96.0% | 84.0% | 84.0% | 65.3% | 45.3% | 34.0% | 14.7% |

  - At 128K, context-management techniques help: Opus 4.5 rose from 34.0% to 40.0% with programmatic tool calling; GPT-5.2-Medium rose from 38.7% to 49.3%; Gemini-3-Flash rose from 21.3% to 33.3% with context awareness.
  — [arXiv 2602.07962 (HTML)](https://arxiv.org/html/2602.07962), [abstract](https://arxiv.org/abs/2602.07962)
- **[M]** Du et al., "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval" (EMNLP Findings 2025; models include Claude 3.7 Sonnet, GPT-4o, Gemini 2.0):
  - Performance degrades within the claimed context length even when retrieval is perfect.
  - Llama-3.1-8B lost 24.2% on MMLU padded to 30K tokens, despite 97% retrieval.
  - With whitespace padding instead of text, drops remained: Llama −48% on VarSum, Mistral −30% on GSM8K at 30K. Drops persisted even when the irrelevant tokens were masked.
  — [arXiv 2510.05381](https://arxiv.org/abs/2510.05381)
- **[O]** Claude Code auto-compaction (community reports, not Anthropic documentation):
  - Reports say it triggers at about 83.5% of the window; others cite about 95% or about 80%, depending on version.
  - The `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` environment variable (1–100) reportedly adjusts the threshold.
  - Several GitHub feature requests ask for a configurable threshold (for example "compact_at_percent: 66").
  — [GitHub issue #43981](https://github.com/anthropics/claude-code/issues/43981), [GitHub issue #41818](https://github.com/anthropics/claude-code/issues/41818), [claudefa.st blog](https://claudefa.st/blog/guide/mechanics/context-buffer-management) (search-snippet level, not verified)

### Inferences
- The LOCA-bench curve is the best available evidence for a Claude-specific agentic handoff threshold. It was measured on Opus 4.5:
  - Quality is roughly flat from 16K to 32K (84%).
  - It drops about 19 points by 64K and falls below 50% by about 96K.
  - Caveat: the x-axis is the environment's information size, not the exact fill level of the context window.
- The 4.6-generation retrieval jump (MRCR 93% at 256K) suggests newer Claude models degrade later. Retrieval is not the same as agentic reasoning, however, and no LOCA-style curve for Opus 4.6+/5.x was found.
- Measured evidence plus Anthropic's own guidance supports a conservative design for coding/document sub-agents:
  - Hand off or compact when accumulated working context reaches about 60–100K tokens, even on 1M-window models.
  - Keep sub-agent return summaries at about 1–2K tokens, as Anthropic recommends.
  - The exact number is a judgement call, not a measured optimum.

### Gaps
- No independent agentic long-context curve was found for Claude Opus 4.6/4.7/5/5.5 or Sonnet 4.6/5/5.5.
- Du et al.'s Claude 3.7 Sonnet numbers were not extracted.
- No Anthropic-published curve of quality vs. tokens for agentic tasks was found (only MRCR/GraphWalks).
- Claude Code's official auto-compact threshold is not documented in a primary source I could reach.

## Q4: Agent performance over long trajectories (error build-up, instruction drift, forgetting early constraints)

### Takeaway
Several measured effects compound over long trajectories:
- **Multi-turn underspecification:** about 39% average drop when information arrives over several turns instead of all at once.
- **Self-conditioning:** the per-step error rate rises once earlier mistakes are in the context; thinking/RL models resist this.
- **Repetition of past actions:** observed beyond about 100K tokens in Gemini's Pokémon agent.
- **Premature giving up:** correlates with context length in long-horizon search agents.
- **Tool overload:** more tools in context means worse tool choice.

### Cited Findings
- **[M]** Laban et al. (Microsoft Research and Salesforce), "LLMs Get Lost In Multi-Turn Conversation" (2025; ICLR 2026):
  - Over 200,000 simulated conversations, 15 models including Claude 3.7 Sonnet, GPT-4.1, Gemini 2.5 Pro, DeepSeek-R1 and Llama 4.
  - Average drop of 39% from single-turn to multi-turn ("sharded") instructions across six tasks (coding, SQL, function calling, math, data-to-text, summarization).
  - The cause is mainly unreliability (+112%) rather than lost aptitude (−15%): when LLMs "take a wrong turn ... they get lost and do not recover".
  — [arXiv 2505.06120](https://arxiv.org/abs/2505.06120)
  - o3 fell from 98.1 to 64.1, and models "make assumptions in early turns and prematurely attempt to generate final solutions". — [Drew Breunig, "How Contexts Fail", June 22, 2025](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- **[M]** Sinha, Arun, Goel et al., "The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs" (NeurIPS 2025):
  - Models "self-condition" on their own errors: the per-step error rate rises as the task goes on and more errors sit in the history (shown by injecting artificial errors).
  - Scaling model size does not fix this.
  - RL-trained thinking models (for example Qwen3 thinking) are largely immune.
  — [arXiv 2509.09677](https://arxiv.org/html/2509.09677)
- **[M]** Gemini 2.5 Pokémon agent (Gemini 2.5 technical report): "beyond 100k tokens, the agent showed a tendency toward favoring repeating actions from its vast history rather than synthesizing novel plans". Hallucinated game state led to fixation on impossible goals ("context poisoning"). — [Breunig summary](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html), [Gemini 2.5 report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)
- **[M]** Databricks long-context RAG study: Llama 3.1 405B correctness deteriorated at around 32K tokens, and smaller models earlier (2024 models). — [Breunig summary](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html), [Databricks blog](https://www.databricks.com/blog/long-context-rag-performance-llms)
- **[M]** Tool overload:
  - Berkeley Function-Calling Leaderboard v3: "every model performs worse when provided with more than one tool".
  - A quantized Llama 3.1 8B failed with 46 tools but succeeded with 19, despite fitting in a 16K window.
  — [Breunig summary](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html), [arXiv 2404.15500](https://arxiv.org/abs/2404.15500)
- **[M]** Xia, Wang, Huang, Liu, "Diagnosing and Mitigating Context Rot in Long-horizon Search" (June 2026):
  - Four flagship models; model names not visible in the abstract.
  - Main failure mode is "premature termination": giving up or giving uncertain wrong answers long before the window is full. Its rate "is positively correlated with context length".
  - Context-management methods act as test-time scaling. Parallel sampling with behaviour-aware filtering gained 2.6–4.9%.
  — [arXiv 2606.29718](https://arxiv.org/abs/2606.29718)
- **[M]** LOCA-bench: "agent performance generally degrades as the environment states grow more complex", and context management "can substantially improve the overall success rate". See Q3 for the Claude Opus 4.5 numbers. — [arXiv 2602.07962](https://arxiv.org/abs/2602.07962)
- **[V]** Anthropic on long-running coding agents: later sessions "declare victory early", and agents that try to one-shot the task run out of context mid-feature. Structured progress files, a feature list and git are the recommended fix. — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### Inferences
- For a coding/document agent, the risk is less "it can't find the fact" and more drift:
  - Early wrong assumptions persist (Laban et al.).
  - Errors already in the context raise later error rates (Sinha et al.).
  - Accumulated history crowds out new planning (Pokémon).
- Handoffs with a clean, curated state summary are therefore justified even before retrieval-type limits are reached.
- Starting a fresh context from a summary is a direct countermeasure to self-conditioning, because the record of errors is removed from the context.

### Gaps
- No study was found that measures the number of tool calls (as opposed to tokens) at which Claude 4.x/5.x agents start to drift, or that quantifies "forgetting early constraints" (for example a system-prompt rule broken after N turns) for Claude specifically.
- Model names and token levels from Xia et al. (2026) were not visible in the abstract.

## Q5: Is "lines read" a usable proxy for tokens? Tokens per line of code/LaTeX, and image token costs in Claude

### Takeaway
Lines are a crude proxy: characters per line differ by about 2.5× between file types in this repository (Python 42, LaTeX 68, TikZ 105 characters per line). The current Claude tokenizer (Opus 4.7+) uses about 2.5 characters per token, versus about 3.5 for older models. So 1,000 lines of LaTeX cost roughly 19–27K tokens, and 1,000 lines of Python roughly 12–17K tokens. Images are costed in 28×28-pixel patches. On Claude 4.7+ (high-resolution tier) one screenshot or page render costs up to 4,784 tokens; on older models up to about 1,568.

### Cited Findings
- **[V]** Claude glossary: "a token approximately represents 3.5 English characters". This is the long-standing rule of thumb. — [Claude docs: Glossary](https://platform.claude.com/docs/en/about-claude/glossary)
- **[V]** Current tokenizer (introduced with Opus 4.7): "1M tokens is roughly 555k words or 2.5M Unicode characters". "Models before it fit about 750k words in 1M tokens." 200K tokens is roughly 150K words. — [Claude docs: Opus 5 overview](https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5)
- **[V]** Opus 4.7's new tokenizer maps the same input to roughly 1.0–1.35× as many tokens, depending on content type. — [Anthropic, Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- **[O]** Third-party rules of thumb (mostly OpenAI tokenizers): 100 lines of Python ≈ 1,000 tokens; 100 lines of JavaScript ≈ 700; 100 lines of SQL ≈ 1,150; about 7–8 tokens per line of code with GPT-4's tokenizer. Deep indentation can cost as many tokens as the code itself. — [16x Engineer: Code to Tokens](https://prompt.16x.engineer/blog/code-to-tokens-conversion)
- **[Calc]** Measured on this repository (`git ls-files`, 2026-10-02; tokens = characters ÷ 3.5 for older Claude models, characters ÷ 2.5 for the Opus 4.7+ tokenizer, using the cited ratios):

  | File type | Lines | Chars/line | Tokens/line (÷3.5) | Tokens/line (÷2.5) | Tokens per 1,000 lines |
  |---|---|---|---|---|---|
  | `.tex` | 2,890 | 67.8 | ≈19 | ≈27 | ≈19K–27K |
  | `.py` | 780 | 41.6 | ≈12 | ≈17 | ≈12K–17K |
  | `.tikz` | 223 | 105.2 | ≈30 | ≈42 | ≈30K–42K |
  | `.md` | 1,203 | 89.9 | ≈26 | ≈36 | ≈26K–36K |
  | `.sh` | 167 | 45.7 | ≈13 | ≈18 | ≈13K–18K |

  These are estimates only. No Claude tokenizer was available offline, and LaTeX/TikZ, being heavy in symbols and backslashes, probably tokenize worse than English prose. The token-counting API gives exact numbers. — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (points to the token counting API)
- **[V]** Image cost formula (current docs):
  - Claude reads images as 28×28-pixel patches, so cost = ⌈width/28⌉ × ⌈height/28⌉ visual tokens.
  - Standard tier (models before Claude 4.7): maximum long edge 1568 px, maximum 1,568 tokens.
  - High-resolution tier ("Claude 4.7 and later models", automatic): maximum long edge 2576 px, maximum 4,784 tokens.
  - Larger images are downscaled to fit, keeping the aspect ratio.
  — [Claude docs: Vision](https://platform.claude.com/docs/en/build-with-claude/vision)
- **[V]** Example costs from the docs:

  | Image | Standard tier | High-resolution tier |
  |---|---|---|
  | 200×200 | 64 tokens | 64 tokens |
  | 1000×1000 | 1,296 tokens | 1,296 tokens |
  | 1092×1092 | 1,521 tokens | 1,521 tokens |
  | 1920×1080 | 1,560 tokens (downscaled to 1456×819) | 2,691 tokens (not resized) |
  | 2000×1500 | 1,564 tokens | 3,888 tokens |
  | 3840×2160 | 1,560 tokens | 4,784 tokens (downscaled to 2576×1449) |

  "High-resolution images can use up to roughly three times more visual tokens than the same image on a standard-tier model." Downsampling is recommended when the extra fidelity is not needed. — [Claude docs: Vision](https://platform.claude.com/docs/en/build-with-claude/vision)
- **[V]** Request limits:
  - Maximum 8000×8000 px per image.
  - Above 20 images per request a stricter per-image limit applies; the docs advise keeping both dimensions ≤2000 px.
  - Up to 600 images per API request (100 for 200K-window models); 10 MB per image via the API.
  - Images inside `tool_result` count toward these limits.
  - Earlier images stay in the conversation, and in agent loops the full history is resent on every turn.
  — [Claude docs: Vision](https://platform.claude.com/docs/en/build-with-claude/vision)
- **[V]** Image tokens are included in the context-awareness token budget. — [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)

### Inferences
- **[Calc]** An A4 page rendered at 150 dpi (1240×1754 px):
  - High-resolution tier (Opus 4.7/4.8/5/5.5): ⌈1240/28⌉×⌈1754/28⌉ = 45×63 ≈ **2,835 tokens** (not resized).
  - Standard tier: downscaled to about 33×47 patches ≈ **~1,550 tokens**.
  - At 300 dpi on the high-resolution tier, a page is capped at ≈**4,784 tokens**.
  - So 20 page-render inspections cost about 31K–96K tokens on current models. Image-heavy review loops reach the 60–100K "degradation zone" quickly.
- The old rule tokens ≈ width×height/750 (from the brief; not re-verified in current docs) is numerically close to the current patch formula, because 28×28 = 784 px² per token. It underestimates slightly because of the ceiling rounding, and it ignores the tier caps (1,568 vs. 4,784).
- Recommendation for a handoff metric: count tokens (from API `usage` or the token counting API), not lines read. If a line-based proxy is needed, calibrate it per file type: about 20–27 tokens per LaTeX line and about 12–17 per Python line on current Claude. Add tool-call overhead, such as line-number prefixes in file-read tools, and the thinking blocks that newer models keep in context.

### Gaps
- No primary Anthropic figure for tokens per line of code or LaTeX was found.
- No exact Claude-tokenizer measurement of this repository was possible offline (tiktoken is not installed, and it would not match Claude's tokenizer anyway).
- The historical docs page with the w×h/750 formula and the "~1,600 tokens" cap was not retrieved; the current docs replace it with the 28-px patch formula.
