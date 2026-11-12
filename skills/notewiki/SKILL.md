---
name: notewiki
description: NotebookLM 결과물을 LLM Wiki → Obsidian → qmd 재사용 지식 자산으로 변환. nlwflow CLI를 사용하여 note-wiki, run-from-yaml, doctor, score-report 등 워크플로우를 실행.
trigger: /notewiki
---

# /notewiki

NotebookLM 결과물을 일회성 리포트로 끝내지 않고, **LLM Wiki → Obsidian → qmd** 파이프라인으로 재사용 가능한 지식 자산으로 변환합니다.

**설치 위치:** `C:\Users\%USERNAME%\notebooklm-llm-wiki-flow\`
**CLI 명령어:** `nlwflow`
**기본 Config:** `~/notebooklm-llm-wiki-flow/config/project.yaml`
**Obsidian 볼트:** `C:/옵시디언/지식`
**LLM Wiki:** `C:/옵시디언/지식/LLM-Wiki`

---

## 사용법

```
/notewiki                                          # 환경 점검 (doctor)
/notewiki "<프롬프트>"                              # 기본 note-wiki 실행
/notewiki "<프롬프트>" --source <URL>              # 소스 URL 지정
/notewiki "<프롬프트>" --title "노트 제목"         # 제목 지정
/notewiki "<프롬프트>" --vault <경로>              # Obsidian 볼트 경로 지정
/notewiki "<프롬프트>" --dry-run                   # 실행 없이 플랜만 출력
/notewiki yaml <파일>.yaml                         # YAML 워크플로우 실행
/notewiki yaml <파일>.yaml --dry-run               # YAML 플랜 미리보기
/notewiki score <리포트.md>                        # 리포트 하이라이트 추출
/notewiki init-config                              # 기본 config 파일 생성
/notewiki install-obsidian-kit --vault <경로>      # Obsidian 스타터 킷 설치
```

---

## What You Must Do When Invoked

인자가 없거나 `doctor`/`check`이면 환경 점검을 실행한다. 그 외에는 아래 단계를 따른다.

### Step 1 - 사전 점검 (단일 게이트, 매 호출 최초 1회)

```bash
PYTHONUTF8=1 nlwflow doctor
```

> **[Windows 한글 환경 필수]** 모든 nlwflow 명령은 반드시 `PYTHONUTF8=1` 접두사를 붙여야 한다.
> 없으면 `doctor`가 한글 경로(`C:/옵시디언/...`)를 cp949로 잘못 읽어 `obsidian_vault_exists: False`로 오탐하거나, `–`(en-dash) 등 유니코드 출력 시 `UnicodeEncodeError: 'cp949'` 로 크래시한다.

기본 config 경로: `~/notebooklm-llm-wiki-flow/config/project.yaml`
모든 nlwflow 명령에 `--config "~/notebooklm-llm-wiki-flow/config/project.yaml"` 를 기본으로 추가한다.

명령 자체가 없으면(`command not found`) 그때만 설치를 안내한다:
```bash
pip install -e "~/notebooklm-llm-wiki-flow" -q
```

doctor 결과를 해석해 **플래그가 false인 항목만** 다음과 같이 안내한다 (전부 미리 로그인/설치를 강요하지 않는다):
- `notebooklm: false` → `notebooklm login` 안내 (브라우저 인터랙티브 로그인이라 `!` 접두사로 사용자가 직접 터미널에서 실행해야 함, Claude Code 내에서 대행 불가). 로그인 후 `notebooklm list --json` 으로 확인.
- `qmd: false` → qmd 없음, `--no-qmd-update` 옵션으로 우회 가능
- `obsidian_vault_exists: false` → `--vault` 옵션 또는 config의 `obsidian_vault` 설정 필요
- `wiki_path_exists: false` → config의 `wiki_path` 설정 필요

모든 플래그가 true이면 바로 Step 3으로 진행하고 별도 보고 없이 실행을 이어간다. `/notewiki` 인자 없이 호출된 경우 여기서 종료하고 doctor 결과만 보고한다.

### Step 3a - note-wiki 실행 (`/notewiki "<프롬프트>"`)

```bash
PYTHONUTF8=1 nlwflow note-wiki "<PROMPT>" [--source <URL>] [--title "제목"] [--vault <경로>] [--wiki-path <경로>] [--dry-run] [--no-qmd-update]
```

- 프롬프트에 URL이 포함되어 있으면 자동으로 소스로 인식됨
- URL이 없으면 `--source` 옵션으로 명시해야 함 (없으면 오류)
- Obsidian 볼트 경로가 없으면 인터랙티브 입력을 요청함 → `--vault` 로 미리 지정 권장
- `--dry-run` 으로 먼저 플랜을 확인한 후 실행하는 것을 권장

출력 결과에서 다음을 보고한다:
- 생성된 노트 파일 경로
- manifest 위치
- 다음 단계 (Obsidian에서 열기, qmd 인덱싱 등)

### Step 3b - YAML 워크플로우 실행 (`/notewiki yaml <파일>`)

```bash
PYTHONUTF8=1 nlwflow run-from-yaml <파일>.yaml [--dry-run] [--no-qmd-update]
```

YAML 형식 예시 (`examples/` 폴더 참고):
```yaml
title: 주제 제목
sources:
  - https://example.com/source1
  - https://example.com/source2
question: "핵심 질문?"
wiki_outputs:
  comparison_slug: topic-slug
  comparison_title: 주제 제목
entities:
  - slug: entity-name
    title: 엔티티 이름
    summary: 엔티티 요약
```

### Step 3c - 리포트 스코어 (`/notewiki score <파일>`)

```bash
PYTHONUTF8=1 nlwflow score-report <리포트.md>
```

마크다운 리포트에서 제목, 섹션, 핵심 불릿을 추출하여 보고한다.

### Step 3d - 설정 초기화 (`/notewiki init-config`)

```bash
nlwflow init-config [config/project.yaml]
```

`config/project.example.yaml` 을 복사하여 초기 설정 파일을 생성한다.
생성 후 사용자에게 수정해야 할 필드를 안내한다:
- `obsidian_vault`: Obsidian 볼트 절대 경로
- `wiki_path`: LLM Wiki 절대 경로 (보통 볼트 내 `LLM-Wiki/`)
- `project_name`: 프로젝트 이름

---

## 설정 우선순위

```
환경변수 (NLWFLOW_*) > project.yaml > .env > 기본값
```

주요 환경변수:
- `NLWFLOW_OBSIDIAN_VAULT` — Obsidian 볼트 경로
- `NLWFLOW_WIKI_PATH` — LLM Wiki 경로

---

## 실행 결과 위치

| 산출물 | 위치 |
|--------|------|
| LLM Wiki 노트 | `<wiki_path>/Entity/`, `<wiki_path>/Comparison/`, `<wiki_path>/Checklist/` |
| Raw 소스 | `<wiki_path>/Raw-Source/` |
| 아티팩트 | `./artifacts/` |
| 실행 매니페스트 | `./artifacts/manifest.json` |

---

## 주의사항

- NotebookLM CLI(`notebooklm` 명령)가 없으면 실제 AI 처리는 불가 — `--dry-run` 으로 플랜 확인만 가능
- qmd가 없으면 `--no-qmd-update` 옵션을 사용하여 qmd 인덱싱 단계를 건너뜀
- 소스 URL 없이 `note-wiki` 를 실행하면 오류 발생
