# AI Agent Skills

Claude Code, Codex 같은 **AI 코딩 에이전트**와 함께 개발할 때 필요한 **워크플로우 skill 모음**입니다.

실제 프로젝트에서 반복되는 패턴들—계획 수립, 테스트 주도 개발, 멀티 에이전트 협업, 기술 선택, 학습 관리—을 정리해서 재사용 가능하도록 만들었습니다.

---

## 설치

### 1. 레포 클론

```bash
git clone https://github.com/duol9/ai-agent-skills.git ~/ai-agent-skills
```

### 2. 기존 프로젝트에 활용

각 skill의 `SKILL.md` 파일 내용을:
- Claude Code의 `.claude/skills/` 폴더에 복사
- Codex의 `.codex/skills/` 폴더에 복사
- 또는 프롬프트로 직접 입력

예시:
```bash
# Claude Code
cp ~/ai-agent-skills/writing-plans/SKILL.md ~/.claude/skills/

# 또는 프롬프트로 직접 사용
cat ~/ai-agent-skills/writing-plans/SKILL.md | pbcopy
# → Claude에 paste
```

### 3. 환경 설정 (선택)

일부 skill은 외부 도구를 필요로 합니다:

- **save-learning**: Notion API
  ```bash
  export MOREE_NOTION_TOKEN="your-token"
  export MOREE_NOTION_LEARNING_DB_ID="your-db-id"
  ```

- **dev-scan**: Gemini CLI
  ```bash
  gemini --version
  ```

- **pr_write**: GitHub CLI
  ```bash
  gh --version
  ```

---

## 사용 방법

### 기본 개발 사이클

```
1. 계획 수립           → writing-plans
   ↓
2. 요구사항 명확화     → clarify (필요시)
   ↓
3. 기술 선택           → tech-decision (필요시)
   ↓
4. 테스트 주도 개발    → test-driven-development
   ↓
5. 멀티 에이전트 실행  → subagent-driven-development
   ↓
6. PR 생성             → pr_write
   ↓
7. 학습 기회 제시      → learning-opportunities
   ↓
8. 학습 내용 저장      → save-learning
```

### 각 skill은 독립적으로도 사용 가능

```bash
# 예: 라이브러리 선택이 필요할 때
→ tech-decision 만 실행

# 예: 코드 리뷰할 때
→ dev-scan 으로 커뮤니티 의견 수집

# 예: 강의식 학습이 필요할 때
→ younghan 페르소나 활성화
```

---

## Skills 소개

### 📋 계획 & 분석

#### **writing-plans**
구현 전에 **단계별 계획**을 상세히 작성합니다.
- 각 step을 2-5분 단위로 세분화
- 파일 경로, 코드 스니펫, 실행 결과 포함
- TDD 기반: 실패 테스트 → 구현 → 통과 검증
- 저장: `docs/plans/YYYY-MM-DD-<feature-name>.md`

**언제 사용**: 새 기능, 복잡한 리팩토링, 불확실한 구현

#### **clarify**
모호한 요구사항을 **구체적인 명세**로 변환합니다.
- 목표, 범위, 제약사항, 성공 기준 도출
- 질문 기반 접근 (한 번에 하나씩)
- Before/After 형식으로 저장

**언제 사용**: 사용자 요청이 여럿으로 해석 가능할 때

#### **tech-decision**
기술 선택을 **증거 기반**으로 진행합니다.
- 옵션 비교 (2-4개)
- 평가 기준 명시
- 트레이드오프 분석
- 신뢰도와 위험도 함께 제시

**언제 사용**: 라이브러리/프레임워크/아키텍처 선택

#### **dev-scan**
Reddit, Hacker News, Dev.to, Lobsters에서 **커뮤니티 의견**을 수집합니다.
- 합의(consensus), 논쟁(controversy), 주목할 관점 구분
- 모든 주장에 출처 링크 첨부
- 최소 4-6개 신뢰할 만한 출처 제시

**언제 사용**: 라이브러리/도구에 대한 실제 평가가 필요할 때

---

### 💻 개발 & 구현

#### **test-driven-development**
Red-Green-Refactor 사이클의 **TDD 워크플로우**입니다.
- 테스트 먼저 작성 (실패 확인)
- 최소한의 코드로 통과 (성공 확인)
- 리팩토링 (구조 개선)
- 엣지 케이스와 에러 케이스 검증

**핵심 규칙**: 프로덕션 코드 전에 항상 실패하는 테스트가 있어야 함.

#### **subagent-driven-development**
**계획을 멀티 에이전트로 실행**합니다.
- 각 task마다 독립적인 subagent 사용 (context 격리)
- 2단계 리뷰: spec 준수 검증 → 코드 품질 검증
- 문제 발생 시 루프: implementer → reviewer → fix → re-review
- 최종 검수 단계

**특징**: 한 세션 내에서 계획 → 완전한 구현까지 수행

#### **pr_write**
Git 히스토리와 변경사항을 분석해 **PR을 자동 생성**합니다.
- 현재 브랜치의 모든 커밋 분석
- PR 제목과 본문 자동 생성
- 사용자 승인 후 PR 생성

**주의**: 자동 생성이지만, 사용자 검토 후 생성

---

### 🎓 학습 & 성장

#### **younghan**
**Kim Younghan 강사님 스타일의 교육 모드**입니다.
- 역사적 진화: 문제 → 해결책 이해 순서로 설명
- 코드 직접 제시 대신 "따라 쳐보세요" 유도
- 친근한 수석 개발자 톤
- 실무 중심의 학습

**활성화**: "선생님" 또는 "영한님" 키워드 사용

#### **learning-opportunities**
코딩 중 **학습 기회**를 제시합니다.
- 새 파일/스키마 생성, 아키텍처 결정 후 활성화
- 6가지 연습 유형: 예측, 생성, 추적, 디버깅, 설명, 회상
- 사용자 응답 대기 (힌트 미제공)
- 명확한 피드백 제공

**핵심**: 학습 > 속도, 이해도 향상 중심

#### **save-learning**
세션 중 얻은 **학습 내용을 Notion에 저장**합니다. ⭐ **직접 작성**
- 구조화된 템플릿: 제목, 배경, 트레이드오프, 핵심, 코드
- Notion API를 통한 자동 저장
- 면접 준비용 학습 DB 누적

**설정**: Notion integration token과 DB ID 필요

---

## 구조

```
ai-agent-skills/
├── README.md
├── writing-plans/
│   └── SKILL.md
├── test-driven-development/
│   ├── SKILL.md
│   └── testing-anti-patterns.md
├── subagent-driven-development/
│   ├── SKILL.md
│   ├── spec-reviewer-prompt.md
│   ├── code-quality-reviewer-prompt.md
│   └── implementer-prompt.md
├── clarify/
│   └── SKILL.md
├── tech-decision/
│   └── SKILL.md
├── dev-scan/
│   └── SKILL.md
├── pr_write/
│   └── SKILL.md
├── younghan/
│   └── SKILL.md
├── learning-opportunities/
│   └── SKILL.md
├── save-learning/
│   ├── SKILL.md
│   └── save_to_notion.py
├── claude-orchestrator/
│   └── (Claude Code 설정 관련)
└── commands/
    └── (CLI 명령어 모음)
```

---

## 출처 & 라이선스

### 직접 작성

- **save-learning**: Notion API 통합 학습 저장 시스템 (100% 자작)

### 참고 & 개인화

다음 skill들은 공개된 프로젝트/방법론을 참고해서 **개인 워크플로우에 맞게 개선**했습니다:

| Skill | 원본 | License | 개선 사항 |
|-------|------|---------|----------|
| **clarify** | [team-attention/plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) | MIT | 한국 개발 요구사항 형식 추가, 예시 현지화 |
| **learning-opportunities** | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) | MIT | 한국 개발 문맥 반영, 실무 사례 추가 |
| **younghan** | [Kim Younghan - Inflearn 강의](https://www.inflearn.com/instructors/108) | 교육 철학 적용 | Spring/Java 강의 철학을 AI 학습 모드로 변환 |

### 기타 Skills

다음 skills의 출처 정보는 현재 검토 중입니다:
- writing-plans
- test-driven-development
- subagent-driven-development
- tech-decision
- dev-scan
- pr_write

---

## License

**MIT License**

이 프로젝트의 모든 파일은 MIT 라이선스를 따릅니다.
참고한 오픈소스 프로젝트의 라이선스도 상단의 표에 명시되어 있습니다.

---

## 사용 예시

### 예시 1: 새 기능 개발 (풀 사이클)

```bash
# 1. 계획 작성
# "새로운 사용자 인증 시스템을 설계해줘"
→ writing-plans 실행
→ docs/plans/2026-06-01-auth-system.md 생성

# 2. 요구사항 확인 (필요시)
# "범위를 명확히 해줄래?"
→ clarify 실행

# 3. 구현 실행
→ subagent-driven-development 실행
  - 각 task 순차 실행
  - spec 검증, 코드 품질 검증

# 4. PR 생성
→ pr_write 실행
→ GitHub PR 자동 생성

# 5. 학습 저장
# "배운 내용을 저장해줄래?"
→ save-learning 실행
→ Notion에 저장
```

### 예시 2: 기술 선택

```bash
# "Redis vs Memcached vs Local cache 중 뭘 쓸까?"
→ tech-decision 실행
→ 평가 기준, 트레이드오프, 리스크 분석
→ 추천과 함께 next step 제시
```

### 예시 3: 커뮤니티 의견

```bash
# "개발자들이 X 라이브러리를 어떻게 평가하고 있어?"
→ dev-scan 실행
→ Reddit, HN, Dev.to, Lobsters에서 수집
→ 출처와 함께 합의, 논쟁, 주목할 의견 제시
```

---

## 지원 & 기여

### 문제 보고

GitHub Issues를 사용하세요:
- Bug report: skill이 제대로 작동하지 않을 때
- Feature request: 새로운 skill 아이디어
- Documentation: README/SKILL.md 개선 제안

### 기여

Pull request는 환영합니다:
1. Fork한 후 feature branch 생성
2. 변경사항 추가
3. PR 제출

---

## FAQ

**Q: 상용 프로젝트에 써도 되나?**
A: 네, MIT 라이선스입니다. 자유롭게 사용, 수정, 배포 가능합니다.

**Q: 특정 언어/프레임워크용인가?**
A: 아니요, 언어/프레임워크 중립적입니다. Python, Java, JavaScript, Go 등 모두 사용 가능합니다.

**Q: 모든 skill을 다 써야 하나?**
A: 아니요, 필요한 것만 선택해서 사용하세요. 각 skill은 독립적입니다.

**Q: 기존 프로젝트에 도입하려면?**
A: `SKILL.md` 내용을 agent 설정에 복사하거나, 프롬프트로 직접 입력하면 됩니다.

---

## 유지보수

이 프로젝트는 실제 개발 프로젝트에서 지속적으로 사용하고 개선 중입니다.

**작성자**: duol9 (lhyy0195@gmail.com)  
**라이선스**: MIT
