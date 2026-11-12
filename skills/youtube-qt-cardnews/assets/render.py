import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

# 사용법: python render.py cards.html 출력폴더 [파일접두어]
src, out = Path(sys.argv[1]), Path(sys.argv[2])
prefix = sys.argv[3] if len(sys.argv) > 3 else "qt"
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(src.resolve().as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    for i in range(1, 5):
        el = pg.locator(f"#c{i}")
        # 넘침 검사: 카드 밖으로 글이 나가면 중단
        assert el.evaluate("e => e.scrollHeight <= e.clientHeight"), f"card {i} overflows"
        el.screenshot(path=str(out / f"{prefix}_{i}.png"))
    b.close()
print("ok")
