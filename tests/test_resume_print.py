import os
import pytest
from playwright.sync_api import Page, expect

def test_en_resume_pdf_export(page: Page):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/resume/index.html"))
    page.goto(f"file://{file_path}")
    
    # Check if the title is right or some content exists
    expect(page.locator("text=Ho Hai Nghia").first).to_be_visible()
    
    # Generate PDF to ensure the print stylesheet works and no errors are thrown
    pdf_path = "/tmp/resume_en_test.pdf"
    page.pdf(path=pdf_path, format="A4", print_background=True)
    
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 1000  # Should be larger than 1KB

def test_vi_resume_pdf_export(page: Page):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/resume/index_vi.html"))
    page.goto(f"file://{file_path}")
    
    expect(page.locator("text=Ho Hai Nghia").first).to_be_visible()
    
    pdf_path = "/tmp/resume_vi_test.pdf"
    page.pdf(path=pdf_path, format="A4", print_background=True)
    
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 1000
