---
description: Save a short technical learning to TIL in the Obsidian devlog vault
---

Save a short technical learning to the TIL section of the Obsidian devlog vault.

## Why we write this

TIL is raw material that shows technical depth for a portfolio.
The goal is to show "this person digs into the why."
Not just how something works — but why it works that way.

## Flow

1. Based on the conversation context, generate a short TIL note.
   Keep it concise — this is a quick "learned this today" memo, not a deep analysis.

2. Show the draft to the user and ask: "이 내용으로 저장할까?"

3. On confirmation:
   - Determine a short, descriptive filename in kebab-case (e.g. `redis-ttl-reset-on-expire`)
   - Save to: `~/Documents/devlog/TIL/YYYY-MM-DD-[title].md`
   - Run: `cd ~/Documents/devlog && git add . && git commit -m "til: [title]" && git push`

---

## Template

```
## 무엇을 알게 됐나?

## 왜 이게 중요한가? (선택)

## 참고 (선택)
```

---

## Tone rules

- Avoid assertive expressions ("맞다", "반드시") — use measured confidence ("적절하다", "안전하다", "일반적이다")
- Keep sentences short and clear
- No emotional or exaggerated expressions
- Always include the reason in one sentence
- Write from practical experience

## Format

- Core explanation: 1-2 sentences
- Reason: 1 sentence

Example:
외부 API DTO에는 사용하는 게 더 안전하다.
API가 필드를 추가하더라도 애플리케이션이 깨지지 않도록 하기 위해서다.
