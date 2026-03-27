---
description: Read all devlog records and update Career portfolio summary
---

Read all accumulated devlog records and update the Career portfolio summary.

## Flow

1. Read all files under `~/Documents/devlog/Projects/` recursively.

2. Analyze the records and extract:
   - Key technical achievements and decisions
   - Problems solved and how (be specific: numbers, scale, context)
   - Technologies used and why (trade-offs made)
   - Business or service impact
   - Growth and insights gained

3. Show the user a summary of what you found and ask: "이 내용으로 portfolio-summary.md 를 업데이트할까?"

4. On confirmation, update `~/Documents/devlog/Career/portfolio-summary.md`:
   - Preserve existing content — append or refine, do not overwrite blindly
   - Focus on "what you were trying to achieve and what you learned", not just "what you did"
   - Highlight technical judgment calls, CS knowledge applied, and business impact

5. Run: `cd ~/Documents/devlog && git add . && git commit -m "career: update portfolio summary" && git push`

---

## Template

```
# Portfolio Summary

## [프로젝트명]
### 어떤 문제를 풀었나?

### 주요 기술 선택과 이유

### 인사이트 & 어필 포인트

---
```

