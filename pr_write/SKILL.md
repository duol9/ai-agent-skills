## allowed-tools: Bash(git log:*), Bash(git diff:*), Bash(git branch:*), Bash(git status:*), Bash(gh pr create:*), Bash(gh pr view:*)
description: 현재 브랜치의 커밋과 변경 사항을 분석하여 PR 제목과 본문을 한국어로 작성하고, 사용자 검토 후 GitHub PR을 생성합니다.

---

## Context

현재 Git 상태를 분석합니다.

- 현재 브랜치: !`git branch --show-current`
- 베이스 브랜치(develop)와의 커밋 목록: !`git log origin/develop..HEAD --oneline`
- 커밋 상세 내용: !`git log origin/develop..HEAD --pretty=format:"%h %s" --name-status`
- 변경된 파일 diff 요약: !`git diff origin/develop...HEAD --stat`
- 워킹 트리 상태: !`git status --short`

---

## Your task

다음 순서로 작업을 진행합니다.

---

## 1단계: 브랜치 분석

현재 브랜치명을 확인합니다.

예시

```
feature/spring-security
```

---

## 2단계: PR 제목 작성

PR 제목 형식

```
[<Tag>/<branch-name>]: <subject>
```

규칙

- `<Tag>` 는 아래 태그 중 가장 적합한 것을 선택합니다.
- `<branch-name>` 은 현재 브랜치명에서 prefix(`feature/`, `fix/` 등)를 제거한 뒤쪽 이름을 사용합니다.
- `<Tag>` 는 아래 표에 정의된 대소문자 그대로 사용합니다.
- `<subject>` 는 한국어로 간결하게 작성합니다.
- 커밋 메시지와 diff 내용을 기반으로 작성합니다.

예시

```
[Feature/store-entity] Store 관련 Entity 생성
```

---

## 사용 가능한 태그

| 태그 | 사용 시점 |
| --- | --- |
| `Feature` | 새로운 기능 추가, 기존 기능의 요구 사항에 맞춘 수정 |
| `Fix` | 기능에 대한 버그 수정 |
| `Chore` | 패키지 매니저 수정, 기타 변경 사항 |
| `Docs` | 문서(주석) 수정 |
| `Style` | 코드 스타일, 포맷팅 수정 (기능 변경 없음) |
| `Refactor` | 기능 변화 없이 코드 리팩터링 |
| `Release` | 버전 릴리즈 |
| `Merge` | 자신의 브랜치에 다른 브랜치를 병합한 경우 |

---

## 3단계: PR 본문 작성

아래 템플릿을 사용합니다.

```md
# What
- 이 PR이 무엇인지

# Why
- 왜 이 작업이 필요했는지

# 변경사항
- (선택) 무엇을 변경했는지


---

## 4단계: 사용자 검토

PR을 바로 생성하지 않습니다.

다음 내용을 사용자에게 먼저 보여줍니다.

- PR 제목
- PR 본문

그리고 아래처럼 검토를 요청합니다.

```
이 제목과 내용으로 PR을 생성할까요?
```

규칙

- 사용자가 수정 요청하면 반영합니다.
- 사용자가 명확히 생성 요청하기 전까지 `gh pr create`를 실행하지 않습니다.

---

## 5단계: PR 생성

사용자가 생성 요청하면 다음 명령으로 PR을 생성합니다.

```bash
gh pr create \
  --base develop \
  --title "<PR 제목>" \
  --body "<PR 본문 전체>"
```

PR 생성 후

- PR URL을 확인합니다.
- 생성된 PR URL을 사용자에게 출력합니다.
