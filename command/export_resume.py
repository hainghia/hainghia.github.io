from __future__ import annotations

import argparse
import re
from pathlib import Path

from weasyprint import CSS, HTML


def main() -> None:
    parser = argparse.ArgumentParser(description="Xuất CV tiếng Anh từ HTML sang PDF.")
    parser.add_argument("output", type=Path)
    output = parser.parse_args().output.resolve()
    source = Path(__file__).resolve().parents[1] / "src/resume/index.html"
    if output.suffix.lower() != ".pdf":
        parser.error("Đường dẫn đầu ra phải có đuôi .pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    content = re.sub(
        r"https://hainghia\.github\.io/+images/",
        "../images/",
        source.read_text(encoding="utf-8"),
    )
    HTML(string=content, base_url=source.parent.as_uri() + "/").write_pdf(
        target=str(output),
        stylesheets=[
            CSS(
                string="""
                @page { size: A4; }
                body { font-size: 10pt; }
                .container, .row, div[style*="flex-direction: column"] {
                    display: block !important;
                }
                .col-4 { float: left; width: 33.333333% !important; }
                .col-6 {
                    width: 66.666667% !important;
                    margin-left: 33.333333%;
                }
                .col-10 { clear: both; }
                """
            ),
        ],
    )


if __name__ == "__main__":
    main()
