from sqlalchemy.orm import Session
from ..models.claim import Claim
from ..schemas import ClaimCreate

class ClaimService:
    def create_claim(self, db: Session, claim: ClaimCreate):
        db_claim = Claim(**claim.dict())
        db.add(db_claim)
        db.commit()
        db.refresh(db_claim)
        return db_claim
