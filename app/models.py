from sqlalchemy import Column, Integer, String
from app.database import Base


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    blood_group = Column(String, nullable=False)
    type = Column(String, nullable=False)  # donate or need
