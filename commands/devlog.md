Save the current conversation's insight, troubleshooting, or decision to the Obsidian devlog vault.

## Flow

1. Ask the user: "어떤 프로젝트야?" (free text input)

2. Ask the user to choose a note type:
   - `troubleshooting` - problem-solving record
   - `feature-log` - feature or task record
   - `ai-usage` - AI usage insights
   - `decision` - decision-making record

3. Based on the conversation context, generate a draft note using the matching template below.
   Fill in each section from the conversation. Omit sections that are not applicable.

   When writing the insight section, reflect these perspectives where relevant:
   - Be specific about the problem (numbers, context, scale)
   - Business/service impact: how did this work affect the service or team?
   - What CS knowledge or technical judgment was applied (data structures, networking, DB, REST/gRPC, etc.)
   - For legacy/refactoring work: what was broken before, and what changed after?

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
```

### feature-log
```
## 왜 이게 필요했나?
> 어떤 문제를 풀려 했나? 누구의 불편함인가?

## 내가 이루려 한 것

## 과정 & 선택들
> 왜 이 기술/방식을 골랐나? 트레이드오프

## 인사이트
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
```
