---
description: Read all devlog records and update Career portfolio summary
---

Read all accumulated devlog records and update the Career portfolio summary.

## Flow

1. Read all files under `~/Documents/devlog/Projects/` recursively.

2. Analyze the records and extract:
   - Key technical achievements and decisions
   - Problems solved and how
   - Technologies used and why
   - Growth and insights gained
   - Business/product impact where mentioned

3. Show the user a summary of what you found and ask: "이 내용으로 portfolio-summary.md 를 업데이트할까?"

4. On confirmation, update `~/Documents/devlog/Career/portfolio-summary.md` using the template below.
   - Preserve existing content — append or refine, do not overwrite blindly.
   - Focus on "무엇을 이루려 했고 무엇을 배웠는지" not just "무엇을 했는지".

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
