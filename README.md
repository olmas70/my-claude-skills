# 내 Claude 활용 모음

자주 쓰는 Claude 프롬프트·명령어·단축키·스킬·플러그인·에이전트·MCP를 한 곳에 모아 두고 바로 복사해 쓰는 페이지입니다.

- `index.html`: 웹페이지 한 장 (GitHub Pages로 배포, 외부 라이브러리 없음)
- `skills.json`: 전체 항목 목록. 한 항목 = 한 줄
  - `id` 이름 · `category` 탭 · `source` 배지(공식/커뮤니티/내 스킬/내장/플러그인/에이전트/MCP/프롬프트/단축키) · `desc` 한 줄 설명 · `invoke` 복사되는 문구
  - `path` 파일 경로(저장소 안 또는 raw.githubusercontent 원본) 또는 `url` 링크만
- `skills/<이름>/SKILL.md`: 내 스킬 원문. 공식·커뮤니티 스킬은 원본 저장소에서 그때그때 불러옵니다(복사본 없음)
- `agents/<이름>.md`: 내 에이전트 정의

## 사용 방법

| 상황 | 방법 |
|---|---|
| 평소 복사해서 쓸 때 | https://olmas70.github.io/my-claude-skills/ 에 접속 (북마크 추천). `/` 키로 검색창 이동, 탭은 주소에 남아 북마크 가능 |
| 항목 추가·삭제할 때 | Claude에게 요청 → `skills.json` 수정·링크 확인 후 push (1~2분 뒤 반영) |
| 직접 수정 후 올리기 전 확인할 때 | 이 폴더에서 `python -m http.server` 실행 → http://localhost:8000 접속 |

> `index.html`을 더블클릭(`file://`)으로 열면 `skills.json`을 못 읽어 카드가 표시되지 않습니다. 미리보기는 위 방법을 쓰세요.
