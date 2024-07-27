from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..schemas import Claim, ClaimCreate
from ..models.claim import Claim as ClaimModel

router = APIRouter()

@router.post("/", response_model=Claim)
def create_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    db_claim = ClaimModel(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim
