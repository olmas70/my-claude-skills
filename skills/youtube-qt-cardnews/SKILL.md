---
name: youtube-qt-cardnews
description: 유튜브 QT/설교 영상 주소 하나로 요약 → 모바일 txt → 큐티 카드뉴스 4장(PNG)까지 한 번에 만든다. 트리거 - 유튜브 링크와 함께 "QT 카드뉴스", "큐티 정리 전체", "요약하고 카드뉴스까지", "/youtube-qt-cardnews".
---

# YouTube QT → 요약 → 모바일 txt → 카드뉴스

## When to Use
- 사용자가 유튜브 QT·설교 영상 링크를 주고 요약, 모바일 txt, 카드뉴스를 한 번에 원할 때
- 세 단계 중 일부만 원하면 해당 단계만 실행한다

## How It Works

바탕화면 경로: `C:\Users\%USERNAME%\OneDrive\바탕 화면` (아래 `DESK`)
스킬 폴더: `~/.claude/skills/youtube-qt-cardnews` (아래 `SKILL`)

### 1단계: 자막 추출 + 요약
```bash
summarize "<URL>" --youtube auto --extract-only > "<scratchpad>/transcript.txt"
```
- 영어 자막만 나올 때가 많다. 직접 읽고 한국어로 요약한다(외부 모델 호출 불필요).
- 자막이 길면 `grep -v '^\s*$'` 후 `sed -n`으로 나눠 끝까지 읽는다. 간증 부분을 빠뜨리지 말 것.
- 채팅 요약 형식:
  - **한 줄 요약** (설교자, 본문, 핵심 메시지)
  - 설교 대지 1·2·3 (절 범위 포함, 각 2~3개 불릿)
  - 적용 질문 3개
  - 성도 간증 (있으면)
  - 끝에 "유튜브 영어 자막 기반이라 원문 표현과 다를 수 있음" 한 줄

### 2단계: 모바일 txt
- 저장: `DESK\QT요약_{책약어}{장}장{절범위}_모바일.txt` (예: `QT요약_고전9장1-12_모바일.txt`)
- 형식은 `SKILL/assets/mobile-example.txt`를 그대로 따른다:
  - 이모지 금지, 마크다운 기호(`**`, `##`, 표) 금지
  - 한 줄 약 20자 이내, 섹션은 `[1] [2] [3]`, 구분선 `------------------------------`
  - 불릿은 `- `, 이어지는 줄은 공백 2칸 들여쓰기
- 저장 후 이모지 0개 확인:
```bash
python -c "import re,sys;t=open(sys.argv[1],encoding='utf-8').read();print(len(re.findall('[\U0001F000-\U0001FFFF\u2600-\u27BF]',t)))" "<파일>"
```

### 3단계: 카드뉴스 4장 (큐티 묵상 디자인)
1. 폴더 생성: `DESK\카드뉴스_{책약어}{장}_{절범위}\` 에 `SKILL/assets/cards.html`, `render.py` 복사
2. `cards.html`의 `<body>` 아래 4개 `<section>` 내용만 교체 (CSS는 건드리지 않음):
   - c1 표지: 날짜(오늘, `date`로 확인), 본문 범위, 2줄 제목, 3줄 부제, 핵심 구절 인용, 키워드 칩 3개
   - c2 말씀: 핵심 절 5개, 개역한글, 강조구는 `<b>`, 생략 절 표시
   - c3 묵상: 대지 3개 타임라인(키워드·절범위 / 한 줄 제목 / 2줄 설명) + 결론 박스
   - c4 적용·기도: 체크박스 3개(하나는 간증에서) + 영상 기도 기반 3~4문장 기도
   - 워터마크 `QT · 1 COR 9` 형식(영문 책 약어 + 장)
3. 렌더 (넘침 검사 포함, Playwright + Chrome 필요):
```bash
cd "<카드폴더>" && python render.py cards.html images {영문약어소문자}{장}   # 예: cor9
```
4. 4장 모두 Read로 열어 눈으로 확인. 줄 끝에 한 글자만 남는 강조구는 `&nbsp;`로 묶고 재렌더.

### 마무리 보고
- txt 경로, 카드 PNG 폴더 경로, 카드별 내용 표
- 개역한글 본문은 기억으로 작성했으므로 성경과 대조 권장 문구 포함

## Examples
- 입력: `/youtube-qt-cardnews https://youtu.be/ky15HbJ2vxw`
- 결과:
  - 채팅 요약 (고린도전서 9:1-12, "범사에 참습니다")
  - `DESK\QT요약_고전9장1-12_모바일.txt`
  - `DESK\카드뉴스_고전9_1-12\images\cor9_1.png` ~ `cor9_4.png`
