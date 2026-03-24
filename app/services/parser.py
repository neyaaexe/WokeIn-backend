import pdfplumber

def extract_pdf(file):
    file.seek(0)
    try:
        with pdfplumber.open(file) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text
    except Exception:
        return ""  