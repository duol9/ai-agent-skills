---
description: Save a short technical learning to TIL in the Obsidian devlog vault
---

Save a short technical learning to the TIL (Today I Learned) section of the Obsidian devlog vault.

## Flow

1. Based on the conversation context, generate a short TIL note. Keep it concise — this is a quick "오늘 이거 알았다" memo, not a deep analysis.

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
