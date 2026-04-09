# Evaluation Criteria

Use a short set of criteria that matches the user's context. Do not score everything just because it exists.

## Common Criteria

- `Delivery speed`: how quickly the team can ship with this option
- `Learning curve`: onboarding and day-2 productivity cost
- `Maintainability`: long-term clarity, upgrade path, and ecosystem stability
- `Performance`: runtime cost, latency, throughput, and footprint
- `Operational complexity`: deployment, observability, debugging, and failure modes
- `Ecosystem maturity`: docs, libraries, community knowledge, hiring pool
- `Compatibility`: fit with the current stack, hosting, and constraints
- `Cost`: licensing, hosting, engineering time, and migration expense
- `Risk`: lock-in, churn, breaking changes, and organizational fragility

## How To Pick

- Greenfield work: weight delivery speed, maintainability, and ecosystem maturity higher.
- Existing codebase: weight compatibility and migration risk higher.
- Scale-sensitive systems: weight performance and operational complexity higher.
- Small team: weight simplicity and maintainability higher.
- Regulated or high-stakes systems: weight reliability, auditability, and operational predictability higher.

## Scoring Guidance

- Use simple qualitative ratings unless the user wants a formal score.
- If you assign weights, keep them rough and explain the rationale.
- Avoid fake precision. `High/Medium/Low` or 1-5 scales are usually enough.

## Red Flags

- A criterion is included but not actually relevant to the user's situation.
- Scores look precise without enough evidence.
- Community hype is being treated as a substitute for technical fit.
- The decision is framed as irreversible when it is actually reversible.
