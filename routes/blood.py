from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from app.utils import get_current_admin
from app.cache import get_from_cache, set_to_cache

router = APIRouter(prefix="/blood", tags=["Blood"])


@router.post("/", response_model=schemas.BloodRequestOut)
def submit_request(request: schemas.BloodRequestCreate, db: Session = Depends(get_db)):
    return crud.create_blood_request(db, request)


@router.get("/donors", response_model=list[schemas.BloodRequestOut])
def get_donors(
    db: Session = Depends(get_db), current_admin: str = Depends(get_current_admin)
):
    cache_key = "blood_request:donors"
    cache_data = get_from_cache(cache_key)
    if cache_data:
        return cache_data

    donors = crud.get_requests_by_type(db, "donate")

    serialized = [
        schemas.BloodRequestOut.model_validate(d).model_dump() for d in donors
    ]

    set_to_cache(cache_key, serialized)
    return serialized


@router.get("/recipients", response_model=list[schemas.BloodRequestOut])
def get_recipients(
    db: Session = Depends(get_db), current_admin: str = Depends(get_current_admin)
):
    cache_key = "blood_request:recipients"
    cache_data = get_from_cache(cache_key)
    if cache_data:
        return cache_data

    recipients = crud.get_requests_by_type(db, "need")

    serialized = [
        schemas.BloodRequestOut.model_validate(r).model_dump() for r in recipients
    ]

    set_to_cache(cache_key, serialized)
    return serialized
