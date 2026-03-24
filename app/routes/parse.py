from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_pdf
from app.services.sentence import get_sentences
from pdfplumber.pdf import PdfminerException

router = APIRouter()

@router.post("/parse")
async def parse_resume(resume: UploadFile = File(...)):
    try:
        text = extract_pdf(resume.file)
    except PdfminerException:
        text = ""  # handle empty or invalid PDF gracefully
    sentences = get_sentences(text)

    return {
        "text": text[:1000],
        "sentences": sentences[:10]
    }
