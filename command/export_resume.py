from __future__ import annotations

import argparse
import re
from pathlib import Path

from weasyprint import CSS, HTML


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Xuất CV từ HTML sang PDF bằng WeasyPrint."
    )
    parser.add_argument("output", type=Path, help="Đường dẫn file đầu ra (.pdf)")
    parser.add_argument(
        "--lang",
        choices=["en", "vi"],
        default=None,
        help="Ngôn ngữ xuất CV (mặc định suy luận từ output name hoặc 'en')",
    )
    args = parser.parse_args()
    output = args.output.resolve()

    if output.suffix.lower() != ".pdf":
        parser.error("Đường dẫn đầu ra phải có đuôi .pdf")

    lang = args.lang
    if not lang:
        if "vi" in output.stem.lower():
            lang = "vi"
        else:
            lang = "en"

    source_dir = Path(__file__).resolve().parents[1] / "src/resume"
    source = source_dir / ("index_vi.html" if lang == "vi" else "index.html")

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
                @page {
                    size: A4;
                    margin: 12mm 10mm;
                }
                body {
                    font-size: 9.5pt;
                    background: #ffffff !important;
                }
                .no-print {
                    display: none !important;
                }
                .page {
                    width: 100% !important;
                    max-width: 100% !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    box-shadow: none !important;
                    border: none !important;
                }
                h2.section-heading, .company-header {
                    break-after: avoid !important;
                    page-break-after: avoid !important;
                }
                .project-entry, .teaching-card {
                    page-break-inside: avoid !important;
                    break-inside: avoid !important;
                }
                """
            ),
        ],
    )
    print(f"Đã xuất CV ({lang.upper()}): {output}")


if __name__ == "__main__":
    main()
