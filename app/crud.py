from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas


def create_blood_request(db: Session, request: schemas.BloodRequestCreate):
    db_request = models.BloodRequest(**request.model_dump())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def get_requests_by_type(db: Session, request_type: str):
    return (
        db.query(models.BloodRequest)
        .filter(func.lower(models.BloodRequest.type) == request_type.lower())
        .all()
    )
