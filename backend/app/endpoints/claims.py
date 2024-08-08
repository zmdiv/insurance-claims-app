from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..schemas import Claim, ClaimCreate
from ..models.claim import Claim as ClaimModel
from ..services.ocr_service import OCRService
from ..services.ai_service import AIService

router = APIRouter()
ocr_service = OCRService()
ai_service = AIService()

@router.post("/", response_model=Claim)
def create_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    db_claim = ClaimModel(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

@router.post("/process")
async def process_documents(insurance_file: UploadFile = File(...), medical_reports: UploadFile = File(...)):
    # Perform OCR on the documents
    insurance_text = ocr_service.process_image(insurance_file.file.read())
    medical_text = ocr_service.process_image(medical_reports.file.read())

    # Combine texts for AI processing
    combined_text = f"Insurance: {insurance_text}\nMedical: {medical_text}"

    # Use OpenAI to analyze the text
    analysis = ai_service.analyze_text(combined_text)

    return {"analysis": analysis}
