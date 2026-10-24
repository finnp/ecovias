"""Build the self-contained map using only the Python standard library."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "src"
vendor = root / "vendor"
replacements = {
    "/* LEAFLET_CSS */": (vendor / "leaflet.css").read_text(),
    "/* LEAFLET_JS */": (vendor / "leaflet.js").read_text().replace(
        "//# sourceMappingURL=leaflet.js.map", ""
    ),
    "/* APP_CSS */": (source / "map.css").read_text(),
    "/* EMBEDDED_FONTS */": (vendor / "fonts.css").read_text(),
    "ROUTES_JSON": (source / "routes.json").read_text().replace("</", "<\\/"),
}
html = (source / "shell.html").read_text()
for marker, content in replacements.items():
    assert marker in html, f"Missing template marker: {marker}"
    html = html.replace(marker, content)

output = root / "index.html"
output.write_text(html)
print(f"Built {output.name} ({output.stat().st_size:,} bytes)")
