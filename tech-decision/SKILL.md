---
name: tech-decision
description: Analyze technical options and recommend a direction with explicit trade-offs, criteria, and source-backed evidence. Use when the user asks for "기술 의사결정", "A vs B", "비교 분석", "라이브러리 선택", "아키텍처 결정", "트레이드오프", "무엇을 써야 할지", or wants a principled recommendation between technical options.
---

# Tech Decision

## Overview

Make technical decisions in a conclusion-first format. Clarify the decision, inspect relevant local context, research external evidence, score the options against explicit criteria, and recommend a direction with risks and follow-up notes.

## Core Rules

- Start with the decision question, candidate options, and evaluation criteria.
- Put the recommendation first in the final report.
- Use current sources for fast-moving technical topics.
- Distinguish codebase facts, official docs, and community sentiment.
- State confidence and unresolved uncertainty.

## Workflow

1. Define the decision.
- What exactly must be chosen?
- What are the realistic options?
- What constraints matter: timeline, team familiarity, scale, runtime, infra, compliance, migration cost?

2. Establish evaluation criteria.
- Use the user's criteria when provided.
- Otherwise choose a small set from `references/evaluation-criteria.md`.
- Assign rough weights when one dimension matters more.

3. Gather evidence from the right places.
- Local codebase: inspect current stack, patterns, constraints, and integration surface.
- Official docs and primary sources: use the `web` tool when recency matters or documentation may have changed.
- Community sentiment: use `$dev-scan` when practitioner reactions materially affect the decision.

4. Parallelize only when explicitly appropriate.
- If the user explicitly asks for parallel work, delegation, or sub-agents, split research into non-overlapping subtasks.
- Otherwise perform the phases directly in the main thread without spawning sub-agents.

5. Analyze trade-offs.
- Compare options against each criterion.
- Call out where evidence conflicts.
- Separate reversible vs hard-to-reverse decisions.
- Highlight migration and operational burden, not just features.

6. Deliver a conclusion-first memo.
- Use `references/report-template.md` as the default shape.
- Recommendation first, reasoning second.
- Include risks, confidence, and practical next steps.

## Research Guidance

### Codebase Inspection

When a repository is available:
- inspect current dependencies and architecture before recommending a new tool
- prefer `rg`, manifests, lockfiles, and key entry points over broad file dumps
- treat existing team patterns as evidence, not as absolute constraints

### Official Documentation

Use current primary sources for:
- framework capabilities and limitations
- version support and release status
- migration guides
- pricing, licensing, and deployment constraints

### Community Evidence

Use `$dev-scan` when you need:
- practitioner pain points
- adoption sentiment
- operational caveats that docs understate
- recurring failure modes or hidden advantages

If `$dev-scan` is not a strong fit, summarize direct source findings without forcing a community scan.

## Output

Default to a short decision memo with:

1. `Recommendation`
2. `Why`
3. `Criteria and weighting`
4. `Option comparison`
5. `Risks and caveats`
6. `Confidence`
7. `Next steps`

Use tables only when they genuinely improve readability.

## Best Practices

- Prefer 2-4 serious options, not a long list of weak candidates.
- If the user says `A vs B`, compare those first before introducing alternatives.
- Be explicit when one option wins only under certain assumptions.
- If the evidence is thin, say so and reduce certainty.
- For high-stakes decisions, include rollback or migration advice.

## Example Triggers

- `React Query vs SWR 뭐가 나을까?`
- `우리 팀에 Prisma가 맞는지 TypeORM이 맞는지 비교해줘`
- `모놀리스 vs 마이크로서비스 결정해야 해`
- `Next.js App Router 계속 갈지 Remix로 갈지 고민`
