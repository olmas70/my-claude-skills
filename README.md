# 내 Claude 활용 모음

자주 쓰는 Claude 스킬을 카테고리별로 모아 두고 바로 복사해 쓰는 페이지입니다.

- `index.html`: 웹페이지 (GitHub Pages로 배포)
- `skills.json`: 스킬 목록 (카테고리, 설명, 호출 문구, SKILL.md 경로)
- `skills/<이름>/SKILL.md`: 내 스킬 원문. 공식 스킬은 anthropics/skills 원본을 그때그때 불러옵니다(복사본은 보관하지 않음)

## 사용 방법

| 상황 | 방법 |
|---|---|
| 평소 스킬 복사해서 쓸 때 | https://olmas70.github.io/my-claude-skills/ 에 접속 (북마크 추천) |
| 스킬 추가할 때 | Claude에게 요청 → 목록 추가·확인 후 push (1~2분 뒤 반영) |
| 직접 수정 후 올리기 전 확인할 때 | 이 폴더에서 `python -m http.server` 실행 → http://localhost:8000 접속 |

> `index.html`을 더블클릭(`file://`)으로 열면 `skills.json`을 못 읽어 카드가 표시되지 않습니다. 미리보기는 위 방법을 쓰세요.
