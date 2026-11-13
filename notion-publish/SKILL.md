---
name: notion-publish
description: Publish drafts, notes, write-ups, or structured summaries into Notion databases or pages using the Notion API. Use when the user wants content sent to Notion, wants a database entry created from text, or provides a Notion token plus a database/page ID for publishing.
---

# Notion Publish

## Overview

Publish text into Notion in a repeatable way. First inspect the target database schema, then create a page with the right properties, and keep the body formatting simple unless the user asks for a richer layout.

## Workflow

1. Confirm the target.
The input should identify either a database ID or a parent page ID. If the user provides a Notion URL, extract the 32-character ID.

2. Inspect the schema before creating a database page.
Run `scripts/get_database_schema.py` with the Notion token and database ID. Do not guess property names. Match the exact property keys returned by Notion.

3. Normalize the writing before publishing.
Default to a plain, natural tone. Remove obvious "AI blog" phrasing unless the user explicitly wants a formal article style. Prefer short paragraphs over overly structured outlines.

4. Create the page.
Run `scripts/create_page.py` with:
- the Notion token
- the parent database ID or page ID
- the page title
- an optional date property
- optional extra properties as JSON
- the body text file

5. Report the result back to the user.
Include the created Notion page URL and mention any assumptions, such as using only the `이름` and `날짜` properties when the database exposes extra fields.

## Commands

Inspect a database:

```bash
python3 scripts/get_database_schema.py \
  --token "$NOTION_TOKEN" \
  --database-id "<database-id>"
```

Create a database page:

```bash
python3 scripts/create_page.py \
  --token "$NOTION_TOKEN" \
  --database-id "<database-id>" \
  --title "<title>" \
  --date-property "날짜" \
  --date-value "2026-03-20" \
  --body-file /path/to/body.txt
```

Create a page under a parent page instead of a database:

```bash
python3 scripts/create_page.py \
  --token "$NOTION_TOKEN" \
  --page-id "<page-id>" \
  --title "<title>" \
  --body-file /path/to/body.txt
```

## Property Mapping

Use exact Notion property names. Common patterns:

- Title property: usually `이름` or `Name`
- Date property: usually `날짜` or `Date`
- Multi-select property: pass option names as a JSON array in `--properties-json`

Example:

```json
{
  "다중 선택": ["백엔드", "설계"]
}
```

## Resources

- `scripts/get_database_schema.py`: fetch the raw database schema and print a compact property summary
- `scripts/create_page.py`: create a Notion page under a database or page parent from a text body file
- `references/payload-patterns.md`: quick examples for common property payload shapes
