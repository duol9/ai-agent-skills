Save the current conversation's insight, troubleshooting, or decision to the Obsidian devlog vault.

## Why we write this

This devlog captures technical depth and the trace of thought behind decisions.
Not just "what was done" — but **why that choice was made, what was learned, and what would be done differently next time**.
Portfolio and resume content is a byproduct of these records.

Each note type has a different purpose:
- `feature-log` / `troubleshooting` / `decision` → technical judgment, thought process, business context
- `ai-usage` → how AI tools were used, what was learned, impressions from AI trends

**For feature-log / troubleshooting / decision:**
Show thought process, not action lists.
If there are no real users yet (early dev stage), replace impact with intent:
"I made this judgment to create X experience for users" — fill with intention and hypothesis.

**For ai-usage:**
Not a list of how AI was used — capture what was felt and learned while using it.
Show how AI trends are being absorbed and applied.

---

## Flow

1. Ask the user: "어떤 프로젝트야?" (free text input)

2. Ask the user to choose a note type:
   - `troubleshooting` - problem-solving record
   - `feature-log` - feature or task record
   - `ai-usage` - AI usage insights
   - `decision` - decision-making record

3. Based on the conversation context, generate a draft note using the matching template below.
   Fill in each section from the conversation. Omit sections that are not applicable.

   When writing, keep these in mind:
   - **No action listing** — not "used INSERT IGNORE" but "why that choice and what tradeoffs were considered"
   - **Thought process first** — initial hypothesis, failures, turning points, final decision
   - **Intent over impact** — if no users yet, replace impact with "what experience I was trying to create"
   - Be specific about the problem (numbers, context, scale)
   - Show what CS knowledge or technical judgment was applied

4. Show the draft to the user and ask: "이 내용으로 저장할까?"

5. On confirmation:
   - Determine a short, descriptive filename in kebab-case (e.g. `redis-ttl-expiry-bug`)
   - Save to: `~/Documents/devlog/Projects/[project]/[type]/YYYY-MM-DD-[title].md`
   - Run: `cd ~/Documents/devlog && git add . && git commit -m "devlog: [type] [title]" && git push`

---

## Templates

### troubleshooting
```
## 상황 & 왜 이게 문제였나?

## 처음 가설 (틀려도 됨)

## 시도한 것들

## 해결

## 인사이트
> Not a technical fact — how did this experience change my thinking?

## 다음엔 어떻게
> What would I do differently if I faced the same situation again?
```

### feature-log
```
## 왜 이게 필요했나?
> What user/business problem was I solving? (No users yet? → what experience was I trying to create?)

## 내가 이루려 한 것

## 과정 & 선택들
> Why this technology/approach? Include first attempts, failures, turning points.

## 인사이트
> Not a technical fact — how did this experience change my thinking?
```

### ai-usage
```
## 어떤 상황에서, 어떻게 썼나?

## 자동화된 것 vs 인사이트를 준 것

## 인사이트

## 다음에 해보고 싶은 것
```

### decision
```
## 어떤 결정이었나?

## 선택지들

## 왜 이걸 골랐나? (트레이드오프)

## 인사이트
> Not a technical fact — how did this experience change my thinking?
```
