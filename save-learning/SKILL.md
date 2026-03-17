# Learning Content → Save to Notion

Store insights and learnings from the `learning-opportunities` skill into a Notion database.  
Structure the content so it can be used later for interview preparation.

---

## Execution Steps

### 1. Organize Learning Content

Summarize what you learned in this conversation using the following structure:

- **Title**: Core topic (1 line)
- **One-line Summary**: A memorable sentence for quick recall
- **Cause / Background**: Why this issue occurred, and in what context
- **Comparison with Alternatives**: Trade-offs (A vs B) for interview questions like “Why did you choose this?”
- **Insights**: Key takeaways (bullet points)
- **Code Example**: Relevant code (if applicable)
- **Tags**: Related technical keywords

---

### 2. Save to Notion

**Must use Python.**  
Using curl + bash single quotes causes `\n` to be treated as a literal string, breaking code block formatting.

    source ~/.zshrc && python3 << 'EOF'
    import os, json, urllib.request

    token = os.environ["MOREE_NOTION_TOKEN"]
    db_id = os.environ["MOREE_NOTION_LEARNING_DB_ID"]

    children = [
        {
            "object": "block", "type": "callout",
            "callout": {
                "rich_text": [{"text": {"content": "💡 <한 줄 요약>"}}],
                "icon": {"emoji": "💡"}
            }
        },
        {
            "object": "block", "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "원인 / 배경"}}]}
        },
        {
            "object": "block", "type": "paragraph",
            "paragraph": {"rich_text": [{"text": {"content": "<원인/배경 설명>"}}]}
        },
        {
            "object": "block", "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "다른 선택지와 비교"}}]}
        },
        {
            "object": "block", "type": "paragraph",
            "paragraph": {"rich_text": [{"text": {"content": "<A vs B 비교>"}}]}
        },
        {
            "object": "block", "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "인사이트"}}]}
        },
        {
            "object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [{"text": {"content": "<인사이트 1>"}}]}
        },
        {
            "object": "block", "type": "heading_2",
            "heading_2": {"rich_text": [{"text": {"content": "코드 예시"}}]}
        },
        {
            "object": "block", "type": "code",
            "code": {
                "language": "kotlin",
                "rich_text": [{"text": {"content": "<코드>"}}]
            }
        },
    ]

    payload = {
        "parent": {"database_id": db_id},
        "properties": {
            "제목": {"title": [{"text": {"content": "<제목>"}}]},
            "다중 선택": {"multi_select": [{"name": "<태그1>"}, {"name": "<태그2>"}]}
        },
        "children": children
    }

    req = urllib.request.Request(
        "https://api.notion.com/v1/pages",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        },
        method="POST"
    )
    res = json.loads(urllib.request.urlopen(req).read())
    print("✅ Success") if res.get("object") == "page" else print("❌ Failed:", res.get("message"))
    EOF

---

### 3. Verify Result

- If `✅ Success` is printed → done  
- If failed → check error message (usually token expiration or DB permission issue)

---

## Environment Variables

| Variable | Description |
|----------|------------|
| NOTION_TOKEN | Notion API token |
| NOTION_LEARNING_DB_ID | Notion database ID |

> Already registered in `~/.zshrc`. Run `source ~/.zshrc` before use.

---

## Notes

- **Do NOT use curl**  
  → `\n` is treated as a literal string, breaking code formatting  

- **Use Python**  
  → Multiline strings are correctly preserved
