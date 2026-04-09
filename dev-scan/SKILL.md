---
name: dev-scan
description: Collect and synthesize developer reactions from Reddit, Hacker News, Dev.to, and Lobsters for a technical topic. Use when the user asks for "개발자 반응", "커뮤니티 의견", "developer reactions", "community sentiment", "Reddit/HN opinions", or wants evidence-backed community feedback about a library, framework, runtime, tool, or technical trend.
---

# Dev Scan

## Overview

Gather practitioner sentiment across major developer communities and turn it into a source-backed summary. Prefer breadth first, then extract repeated patterns, disagreements, and noteworthy takes with links.

## Workflow

1. Extract the topic from the user's request.
Examples:
- `"React 19 개발자들 반응"` -> `React 19`
- `"Bun vs Deno 커뮤니티 의견"` -> `Bun vs Deno`

2. Search four sources.
- Reddit: prefer `gemini -p "Search Reddit for discussions about <TOPIC>..."` when `gemini` CLI is installed and usable.
- Hacker News, Dev.to, Lobsters: use the `web` tool with targeted queries.

3. Fallbacks.
- If `gemini` CLI is unavailable, unauthenticated, or blocked, fall back to the `web` tool for Reddit with focused queries.
- If one source has weak results, continue with the others and say so.
- Do not fabricate consensus from a single weak thread.

4. Synthesize findings into three buckets:
- `Consensus`: repeated points that appear across multiple sources or strong repeated threads
- `Controversy`: points where opinions clearly diverge
- `Notable Perspective`: unusually concrete, senior, long-term, or edge-case insight

5. Every claim must carry a source link.
- Prefer inline source attribution.
- Distinguish firsthand experience from general opinion.
- Mark recency when it materially affects the topic.

## Search Guidance

### Reddit

Preferred command:

```bash
gemini -p "Search Reddit for discussions about <TOPIC>. Summarize the main opinions, debates, and insights from developers. Include Reddit post URLs where possible. Focus on: 1) common opinions 2) controversies 3) notable perspectives from experienced developers."
```

Notes:
- Prefer one focused Gemini call over several fragmented Reddit calls.
- Use natural-language prompts such as `Search Reddit for...`; do not rely only on `site:reddit.com`.

Fallback Reddit web queries:
- `site:reddit.com <topic> developers opinion`
- `site:reddit.com/r/programming OR site:reddit.com/r/webdev <topic>`

### Other Communities

Use the `web` tool for:
- `site:news.ycombinator.com <topic>`
- `site:dev.to <topic>`
- `site:lobste.rs <topic>`

When the topic is time-sensitive, browse and prefer more recent threads.

## Output Format

Use this structure by default:

```markdown
## Key Insights

### Consensus
1. **[Point]** - [brief explanation]. Sources: [Reddit](url), [HN](url)

### Controversy
1. **[Debate]** - Pro: [summary] ([Source](url)). Con: [summary] ([Source](url)).

### Notable Perspective
1. **[Insight]** - [why it matters]. Source: [Platform](url)

### Gaps
- [missing source, weak evidence, or recency limitation]
```

## Quality Bar

- Prefer at least 4-6 substantive source links total.
- Do not overstate community consensus when evidence is mixed.
- Prefer concrete reports from production use over vague reactions.
- Quote sparingly and stay within source limits.
- If the user is making a decision, end with a short implication section such as `What this means for your decision`.

## When To Drill Deeper

Do a second pass when:
- the topic is controversial
- the user is comparing options
- the first pass produces thin evidence
- the topic appears very new and source recency matters

Second-pass ideas:
- narrow to specific subreddits or communities
- separate beginner sentiment from production sentiment
- separate launch reactions from later retrospective reactions
