# AI Agent Skills

AI 코딩 에이전트(Claude, Codex 등)가 사용할 수 있는 **개발 워크플로우 기반 skill 모음**입니다.

각 skill의 상세 설명은 해당 디렉토리 내부 문서를 참고하세요.

---

## Skills

* **writing-plans**
  개발 작업을 시작하기 전에 구현 계획을 작성하도록 돕는 skill

* **test-driven-development**
  테스트 기반 개발(TDD) 워크플로우를 지원하는 skill

* **subagent-driven-development**
  여러 에이전트를 활용한 협업 기반 개발을 위한 skill

* **claude-orchestrator**
  Claude 에이전트 워크플로우를 구성하기 위한 설정

---

## Installation

레포를 홈 디렉토리에 clone 합니다.

```bash
cd ~
git clone https://github.com/duol9/ai-agent-skills.git
```

설치 경로

```
~/ai-agent-skills
```

---

## Usage

필요한 skill을 Claude 또는 Codex의 skill 디렉토리에 연결하여 사용할 수 있습니다.

예시 경로

```
~/.claude/skills
~/.codex/skills
```

예시

```bash
ln -s ~/ai-agent-skills/writing-plans ~/.codex/skills/writing-plans
```

각 skill의 사용 방법은 해당 디렉토리의 문서를 참고하세요.

---

## Sources

이 저장소는 여러 AI agent skill을 모아 개인적으로 사용하는 형태로 정리한 것입니다.

각 skill의 원본 출처는 다음과 같습니다.

- writing-plans → [(원본 레포 링크)](https://github.com/obra/superpowers/tree/main/skills/writing-plans)
- test-driven-development → [(원본 레포 링크)](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)
- subagent-driven-development → [(원본 레포 링크)](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development)
- claude-orchestrator → [(원본 레포 링크)](https://github.com/gaebalai/claude-code-orchestrator)
