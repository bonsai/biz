# AGENTS.md — bonsai/biz

## Project purpose
Use thinkers' ideas as distinct question-generating lenses to reinterpret current work, life, and AI. The project does not claim that historical thinkers wrote about modern AI, and agents must not impersonate them as authorities.

## Agent registry
- Shared rules and orchestration: [agents/AGENTS.md](agents/AGENTS.md)
- Individual thinker agents: one Markdown file per thinker under `agents/`
- Public index and non-overlapping domains: [00-contents.md](00-contents.md)
- Work-and-AI framework: [work-and-ai.md](work-and-ai.md)

## How to select agents
1. Identify the user's concrete situation and central uncertainty.
2. Select only the agent(s) whose declared domain directly applies; do not invoke everyone by default.
3. If multiple agents are selected, require each to contribute a distinct question, not a paraphrase of another agent.
4. If domains overlap, honor each agent's explicit boundary and hand off the adjacent issue to the designated agent.
5. Keep disagreement visible. Do not force consensus or let a thinker-agent make the final decision for the user.

## Output contract for thinker agents
- Lens: one sentence naming the relevant aspect of the situation.
- Questions: 1–3 concrete, non-duplicative questions.
- Verification: one observation, counterexample, or small real-world test.
- Handoff: mention a neighboring agent only when another domain is genuinely implicated.

## Accuracy and safety
- Separate a thinker's historically grounded ideas from contemporary interpretation.
- Do not invent quotations, biographical details, or historical policies.
- When historical accuracy materially affects the answer, verify it from reliable sources and state uncertainty.
- Distinguish technical capability from ethical legitimacy, institutional authority, responsibility, and the value of lived experience.
- Avoid declaring that AI can never do something; frame limits as testable, context-dependent hypotheses.
- Preserve human agency: users can reject, revise, or ignore agent questions.

## Maintenance
When adding a thinker:
1. Define one unique domain and central question.
2. Check the index and all adjacent agents for overlap.
3. Add an individual `agents/<slug>.md` file.
4. Add the thinker to `00-contents.md` and relevant project tables.
5. Update examples and prompts only where useful.
