import os
from pathlib import Path
import pytest
from playwright.sync_api import Page, expect
from pypdf import PdfReader


RESUME_DIR = Path(__file__).resolve().parents[1] / "src/resume"


def test_en_resume_desktop_view(page: Page):
    """Kiểm tra hiển thị web desktop cho bản tiếng Anh."""
    page.set_viewport_size({"width": 1280, "height": 900})
    file_path = RESUME_DIR / "index.html"
    page.goto(f"file://{file_path.resolve()}")

    expect(page.locator("h1.candidate-name")).to_have_text("Ho Hai Nghia")
    expect(page.locator(".candidate-title")).to_contain_text("Technical Architect")
    expect(page.locator("text=01 / Executive Summary & Architecture Philosophy")).to_be_visible()
    expect(page.locator("text=02 / Technical Competencies")).to_be_visible()
    expect(page.locator("text=03 / Professional Experience")).to_be_visible()
    expect(page.locator("text=Dynamics 365").first).to_be_visible()

    # Verify buttons and switcher
    expect(page.locator(".btn-print")).to_be_visible()
    expect(page.locator(".lang-switcher")).to_be_visible()


def test_vi_resume_desktop_view(page: Page):
    """Kiểm tra hiển thị web desktop cho bản tiếng Việt."""
    page.set_viewport_size({"width": 1280, "height": 900})
    file_path = RESUME_DIR / "index_vi.html"
    page.goto(f"file://{file_path.resolve()}")

    expect(page.locator("h1.candidate-name")).to_have_text("Hồ Hải Nghĩa")
    expect(page.locator(".candidate-title")).to_contain_text("Technical Architect")
    expect(page.locator("text=01 / Tóm tắt Năng lực & Triết lý Kiến trúc")).to_be_visible()
    expect(page.locator("text=02 / Kỹ năng Kỹ thuật Cốt lõi")).to_be_visible()
    expect(page.locator("text=03 / Kinh nghiệm Làm việc Chuyên nghiệp")).to_be_visible()
    expect(page.locator("text=Dynamics 365").first).to_be_visible()


def test_mobile_responsive_view(page: Page):
    """Kiểm tra hiển thị responsive trên thiết bị di động (iPhone viewport)."""
    page.set_viewport_size({"width": 375, "height": 812})
    file_path = RESUME_DIR / "index.html"
    page.goto(f"file://{file_path.resolve()}")

    # Ensure candidate name and header render cleanly
    expect(page.locator("h1.candidate-name")).to_be_visible()
    expect(page.locator(".contact-bar")).to_be_visible()

    # Check horizontal scroll is not overflowing page width
    scroll_width = page.evaluate("document.documentElement.scrollWidth")
    client_width = page.evaluate("document.documentElement.clientWidth")
    assert scroll_width <= client_width + 1, f"Horizontal overflow on mobile: scrollWidth={scroll_width}, clientWidth={client_width}"


def test_en_resume_pdf_export(page: Page, tmp_path: Path):
    """Kiểm tra in ấn và xuất PDF bản tiếng Anh qua Playwright."""
    file_path = RESUME_DIR / "index.html"
    page.goto(f"file://{file_path.resolve()}")

    pdf_path = str(tmp_path / "resume_en.pdf")
    page.pdf(path=pdf_path, format="A4", print_background=True)

    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 1000

    reader = PdfReader(pdf_path)
    assert len(reader.pages) > 0
    full_text = "\n".join(p.extract_text() for p in reader.pages)
    assert "Dynamics 365" in full_text
    assert "Print / PDF" not in full_text

    # Verify no blank pages
    for i, p in enumerate(reader.pages):
        assert len(p.extract_text().strip()) > 0, f"Page {i + 1} is empty in EN PDF!"


def test_vi_resume_pdf_export(page: Page, tmp_path: Path):
    """Kiểm tra in ấn và xuất PDF bản tiếng Việt qua Playwright."""
    file_path = RESUME_DIR / "index_vi.html"
    page.goto(f"file://{file_path.resolve()}")

    pdf_path = str(tmp_path / "resume_vi.pdf")
    page.pdf(path=pdf_path, format="A4", print_background=True)

    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 1000

    reader = PdfReader(pdf_path)
    assert len(reader.pages) > 0
    full_text = "\n".join(p.extract_text() for p in reader.pages)
    assert "Dynamics 365" in full_text
    assert "In / Xuất PDF" not in full_text

    # Verify no blank pages (solving the previous blank page 2 bug)
    for i, p in enumerate(reader.pages):
        assert len(p.extract_text().strip()) > 0, f"Page {i + 1} is empty in VI PDF!"
