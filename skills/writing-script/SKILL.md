---
name: writing-script
description: Create narration scripts for the bonsai/biz series.
---

# 読み上げ原稿執筆スキル

Use this skill when asked for a complete episode script or a substantial rewrite. It owns the finished spoken essay; use `episode-planning` for topic selection and outlining, and `reading-aloud` for polishing an existing script for delivery.

## Before drafting
1. Read `00-contents.md`, `AGENTS.md`, `agents/AGENTS.md`, and the relevant `agents/<slug>.md`.
2. Confirm the episode has one central question and a distinct role within the series. Use the first episode as a reference for accessibility and narrative flow, not as a template to copy: https://github.com/bonsai/biz/blob/main/01-marx-and-ai.md
3. If the figure, question, or differentiation from existing episodes is unclear, plan first with the `episode-planning` skill.
4. Verify historically important claims when needed. Separate historically grounded ideas, present-day interpretation, and uncertain claims.

## Writing principles
1. **Name the figure clearly.** Introduce the figure by full name and explain why their ideas help examine this question now.
2. **One main question.** Choose one primary concern—such as intelligence, work, human/AI complementarity, or appropriate delegation—and keep the essay focused.
3. **Do not impersonate or over-authorize.** Use the figure's thought as a question-generating lens, not as a simulated voice or final authority. Never imply the figure discussed modern AI unless that is historically true.
4. **Ground abstractions in a lived situation.** Choose a concrete example from work, learning, creative practice, care, community, or home.
5. **Separate capability from legitimacy.** Distinguish what a system can do reliably from whether it should be entrusted with a task, who is accountable, and what experience or agency might be lost.
6. **Avoid simplistic human exceptionalism.** Do not present AI limitations as permanent human-only sanctuaries. Describe capabilities and limitations as contextual and testable; distinguish them from social decisions about purpose, authority, and responsibility.
7. **Show complementarity where it is real.** Explore how human purposes, context, lived experience, and judgment can work with AI-supported search, generation, comparison, critique, and synthesis. Do not force a human-versus-AI contest.
8. **Respect agent boundaries.** Consult `agents/AGENTS.md` and the relevant individual agent. Keep the lead figure's unique question central, and make meaningful differences from adjacent agents explicit. Mention the agent/SNS concept only when it genuinely serves the episode.
9. **Use a spoken Japanese style.** Write for listening rather than academic reading: moderate sentence length, clear transitions, explained unfamiliar names and concepts, and few unexplained abbreviations. Headings are acceptable, but the body must read naturally aloud.
10. **End with an open, memorable question.** Avoid turning the figure's name into a guarantee or forcing an overly certain conclusion.

## Suggested narrative arc
- **Opening:** Begin with a recognizable present-day situation affected by AI and surface the listener's dilemma.
- **The historical idea:** Explain only the relevant concept and context; avoid a long biography.
- **Applying the idea today:** Clearly mark the contemporary connection as interpretation or a thought experiment.
- **Human/AI relationship:** Show what AI can support, what people contribute, and what the combination makes possible.
- **Practical implication:** Offer a testable action or condition to check, not a universal prescription.
- **Closing:** Briefly crystallize the tension and leave one strong question.

Adapt this arc when another structure better serves the question. Do not force every episode into identical headings.

## Length and output contract
- Default to 1,800–2,800 Japanese characters unless another length is requested.
- Output the title and finished script only unless the user asks for planning notes or commentary.
- Do not add an explanatory postscript, summary bullets, or meta-commentary after the script.
- Never invent quotations, statistics, anecdotes, biographical details, or historical claims.
- If shortening, preserve the central question, core reasoning, one concrete example, and closing question.
- For speech-only polishing or performance coaching, use `reading-aloud`; do not silently alter the thesis or invent a new episode.
