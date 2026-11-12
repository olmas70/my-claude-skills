---
paths:
  - "src/api/**/*.ts"
  - "tests/api/**/*.ts"
---

# API 코드 규칙

<!-- 프로젝트의 .claude/rules/api.md 로 저장. 위 paths 에 맞는 파일을 읽거나 고칠 때만 불러와져 컨텍스트를 아낀다.
     paths 를 지우면 항상 적용되는 일반 규칙이 된다. 파일 하나에 주제 하나 (예: testing.md, api.md, frontend.md) -->

- 모든 엔드포인트는 입력값을 검증한다 (zod 스키마)
- 오류 응답은 `{ error: { code, message } }` 형식으로 통일
- DB 접근은 파라미터 바인딩만 사용. 문자열로 SQL 조합 금지
- 새 엔드포인트에는 같은 경로의 테스트 파일을 함께 만든다
