---
name: clarify
description: Clarify vague or ambiguous requests into a precise, actionable specification before planning or implementation. Use when the user asks to "clarify", "명확하게 해줘", "요구사항 정리", "specify requirements", "refine requirements", "make this clearer", or when the request is underspecified and important assumptions would otherwise be required.
---

# Clarify

## Overview

Turn a vague request into a concrete requirement with explicit goal, scope, constraints, and success criteria. Ask only the minimum number of questions needed to remove ambiguity.

## Core Rules

- Do not guess critical requirements when a wrong assumption would change the outcome.
- Preserve the user's intent. Clarify it; do not redirect it.
- Ask focused questions, not broad interviews.
- Prefer concrete options over abstract preferences when options are obvious.
- Keep momentum: ask the fewest questions needed to make the next step safe.

## When To Use

Use this skill when:
- the user explicitly asks for clarification or refinement
- the request could mean multiple materially different things
- scope, constraints, or success criteria are missing
- a bug report lacks reproduction details
- implementation would otherwise rely on risky assumptions

Do not use this skill when:
- the request is already specific enough to act on safely
- a reasonable assumption is low-risk and easy to correct later
- the user clearly wants immediate execution and ambiguity is minor

## Workflow

1. Capture the original request exactly enough to preserve intent.

2. Identify the minimum missing pieces from these categories:
- `Goal`: what outcome is wanted
- `Scope`: what is included and excluded
- `Behavior`: key flows, edge cases, error handling
- `Interface`: who interacts and through what surface
- `Data`: inputs, outputs, formats, persistence
- `Constraints`: stack, deadlines, compatibility, performance, policy
- `Success`: how completion will be judged

3. Ask concise follow-up questions.
- Ask 1 question at a time by default.
- Ask up to 3 together only when they are tightly related and easy to answer in one reply.
- Prefer option-shaped questions such as:
  - `로그인은 이메일/비밀번호, OAuth, 매직링크 중 무엇이 필요해?`
  - `CSV만 고치면 돼, 아니면 엑셀 export도 포함이야?`

4. Update the clarified requirement after each answer.
- Remove resolved ambiguities.
- Re-evaluate what still blocks safe action.
- Stop asking as soon as the task becomes actionable.

5. Produce a before/after summary.
- Use `references/clarification-template.md` as the default output shape.
- Keep it short unless the user asks for a fuller spec.

6. Offer persistence only when useful.
- If the user wants the clarified spec saved, write it to a sensible path such as `requirements/` or a project-appropriate docs folder.
- Use a descriptive filename based on the topic.

## Question Design

- Specific over general
- One concern at a time
- Neutral framing
- Concrete nouns over abstract language
- Prefer recognition over recall when natural options exist

Good:
- `관리자만 쓰는 기능이야, 아니면 일반 사용자도 써?`
- `대상은 웹 앱이야, API야, 둘 다야?`

Weak:
- `원하는 방향을 자세히 설명해줘`
- `필요한 걸 전부 말해줘`

## Output

Default structure:

```markdown
## Requirement Clarification Summary

### Before
"[original request]"

### After
**Goal**: ...
**Scope**: ...
**Constraints**: ...
**Success Criteria**: ...

### Decisions Made
| Topic | Decision |
|-------|----------|
| Auth method | OAuth |
| Scope | Login + logout only |

### Open Questions
- ...
```

If enough clarity exists to proceed immediately, finish the summary and then continue with the main task.

## Examples

### Feature Request

Original:
- `로그인 기능 넣어줘`

Likely questions:
- 이메일/비밀번호, OAuth, 매직링크 중 무엇이 필요한가
- 회원가입과 비밀번호 재설정도 포함되는가
- 세션 정책이나 보안 제약이 있는가

### Bug Report

Original:
- `export가 깨졌어`

Likely questions:
- 어떤 export 형식인가
- 실제로 어떤 증상이 나는가
- 언제부터 재현되는가
- 재현 단계가 무엇인가

## Save Guidance

When saving a clarified spec:
- prefer `requirements/` for product or feature requirements
- prefer `docs/` when it belongs with existing project documentation
- use Markdown
- keep the filename descriptive, for example `auth-requirements.md`
