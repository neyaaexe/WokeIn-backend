import PyPDF2
import docx
import pytesseract
from PIL import Image
import tempfile

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def parse_resume(file):
    # Save temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    if file.filename.endswith(".pdf"):
        return extract_text_from_pdf(tmp_path)
    elif file.filename.endswith(".docx"):
        return extract_text_from_docx(tmp_path)
    elif file.filename.endswith((".jpg", ".jpeg", ".png")):
        return extract_text_from_image(tmp_path)
    else:
        raise ValueError("Unsupported file type")