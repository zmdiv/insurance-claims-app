from fastapi import APIRouter, UploadFile, File
from ...services.ocr_service import OCRService

router = APIRouter()

ocr_service = OCRService()

@router.post("/process")
def process_image(file: UploadFile = File(...)):
    content = file.file.read()
    text = ocr_service.process_image(content)
    return {"text": text}
