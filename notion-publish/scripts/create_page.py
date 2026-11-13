#!/usr/bin/env python3
import argparse
import json
import pathlib
import urllib.request


def build_rich_text(text: str) -> list[dict]:
    return [{"type": "text", "text": {"content": text}}]


def build_children(body: str) -> list[dict]:
    blocks = []
    for paragraph in [chunk.strip() for chunk in body.split("\n\n") if chunk.strip()]:
        blocks.append(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": build_rich_text(paragraph)},
            }
        )
    return blocks


def build_properties(title: str, title_property: str, date_property: str | None, date_value: str | None, raw_properties: dict) -> dict:
    properties: dict = {
        title_property: {
            "title": build_rich_text(title),
        }
    }

    for key, value in raw_properties.items():
        if isinstance(value, list):
            properties[key] = {"multi_select": [{"name": item} for item in value]}
        elif isinstance(value, bool):
            properties[key] = {"checkbox": value}
        else:
            properties[key] = {"rich_text": build_rich_text(str(value))}

    if date_property and date_value:
        properties[date_property] = {"date": {"start": date_value}}

    return properties


def notion_post(payload: dict, token: str) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        "https://api.notion.com/v1/pages",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Notion page from a text body.")
    parser.add_argument("--token", required=True)
    parser.add_argument("--database-id")
    parser.add_argument("--page-id")
    parser.add_argument("--title", required=True)
    parser.add_argument("--title-property", default="이름")
    parser.add_argument("--date-property")
    parser.add_argument("--date-value")
    parser.add_argument("--properties-json", default="{}")
    parser.add_argument("--body-file", required=True)
    args = parser.parse_args()

    if bool(args.database_id) == bool(args.page_id):
        raise SystemExit("Provide exactly one of --database-id or --page-id.")

    body = pathlib.Path(args.body_file).read_text(encoding="utf-8")
    extra_properties = json.loads(args.properties_json)

    parent = {"database_id": args.database_id} if args.database_id else {"page_id": args.page_id}
    payload = {
        "parent": parent,
        "children": build_children(body),
    }

    if args.database_id:
        payload["properties"] = build_properties(
            args.title,
            args.title_property,
            args.date_property,
            args.date_value,
            extra_properties,
        )

    response = notion_post(payload, args.token)
    print(json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
