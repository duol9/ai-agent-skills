# Payload Patterns

Use these patterns when building `--properties-json` for `scripts/create_page.py`.

## Plain text field

```json
{
  "설명": "짧은 메모"
}
```

## Multi-select field

```json
{
  "다중 선택": ["백엔드", "설계"]
}
```

## Checkbox field

```json
{
  "공개": true
}
```

## Combined example

```json
{
  "다중 선택": ["아키텍처", "인증"],
  "설명": "온보딩 상태 관리 메모",
  "공개": false
}
```
