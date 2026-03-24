from app.services.parser import extract_pdf
import io

def test_extract_pdf_empty():
    fake_file = io.BytesIO(b"")
    text = extract_pdf(fake_file)
    assert isinstance(text, str)
    