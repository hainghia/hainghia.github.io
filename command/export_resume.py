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
                * {
                    -webkit-print-color-adjust: exact !important;
                    print-color-adjust: exact !important;
                    color-adjust: exact !important;
                }
                @page {
                    size: A4;
                    margin: 10mm 10mm;
                }
                body {
                    font-size: 9pt;
                    background: #ffffff !important;
                    color: #000000 !important;
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
                .header-inner {
                    display: flex !important;
                    flex-direction: row !important;
                    align-items: center !important;
                    text-align: left !important;
                    gap: 16px !important;
                }
                .candidate-avatar {
                    width: 68px !important;
                    height: 68px !important;
                    margin: 0 !important;
                    box-shadow: none !important;
                    border: 1px solid #d4d4d8 !important;
                }
                .resume-header {
                    margin-bottom: 8px !important;
                    padding-bottom: 6px !important;
                }
                .candidate-name {
                    font-size: 18pt !important;
                    margin-bottom: 2px !important;
                    line-height: 1.1 !important;
                }
                .candidate-title {
                    font-size: 9.5pt !important;
                    margin-bottom: 4px !important;
                    color: #3f3f46 !important;
                }
                .contact-bar {
                    font-size: 8pt !important;
                    gap: 4px 10px !important;
                    justify-content: flex-start !important;
                }
                .contact-icon {
                    width: 11px !important;
                    height: 11px !important;
                }
                .section-experience-heading {
                    break-before: page !important;
                    page-break-before: always !important;
                    margin-top: 0 !important;
                }
                h2.section-heading {
                    margin-top: 10pt !important;
                    margin-bottom: 5pt !important;
                    background: #f4f4f5 !important;
                    display: block !important;
                    break-after: avoid-page !important;
                    page-break-after: avoid !important;
                    break-inside: avoid !important;
                    page-break-inside: avoid !important;
                }
                .summary-box {
                    font-size: 8.5pt !important;
                    line-height: 1.4 !important;
                }
                .philosophy-grid {
                    display: grid !important;
                    grid-template-columns: 1fr 1fr !important;
                    gap: 5px 12px !important;
                    margin-top: 5px !important;
                }
                .philosophy-item {
                    font-size: 8pt !important;
                    line-height: 1.35 !important;
                    padding-left: 10px !important;
                }
                .philosophy-item strong {
                    font-size: 8pt !important;
                }
                .skills-table {
                    font-size: 8pt !important;
                    display: table !important;
                    width: 100% !important;
                }
                .skills-table tr {
                    display: table-row !important;
                }
                .skills-table td {
                    display: table-cell !important;
                    padding: 2.5pt 0 !important;
                    line-height: 1.35 !important;
                }
                .skills-table td.cat-name {
                    width: 20% !important;
                    font-size: 8pt !important;
                    font-weight: 700 !important;
                    margin-top: 0 !important;
                }
                .skills-table td.cat-content {
                    width: 80% !important;
                }
                .company-header {
                    break-after: avoid !important;
                    page-break-after: avoid !important;
                }
                .project-entry, .teaching-card {
                    page-break-inside: avoid !important;
                    break-inside: avoid !important;
                }
                .tech-pill-row {
                    background: #f4f4f5 !important;
                    border: 1px solid #e4e4e7 !important;
                }
                """
            ),
        ],
    )
    print(f"Đã xuất CV ({lang.upper()}): {output}")


if __name__ == "__main__":
    main()
