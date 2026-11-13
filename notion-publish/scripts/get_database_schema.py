#!/usr/bin/env python3
import argparse
import json
import urllib.request


def notion_get(url: str, token: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
        },
        method="GET",
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch and print a Notion database schema.")
    parser.add_argument("--token", required=True)
    parser.add_argument("--database-id", required=True)
    args = parser.parse_args()

    database = notion_get(f"https://api.notion.com/v1/databases/{args.database_id}", args.token)
    properties = database.get("properties", {})

    print(json.dumps(database, ensure_ascii=False, indent=2))
    print("\nProperty summary:")
    for name, value in properties.items():
        print(f"- {name}: {value.get('type')}")


if __name__ == "__main__":
    main()
