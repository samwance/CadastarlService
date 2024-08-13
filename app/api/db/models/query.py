from sqlalchemy import Column, Integer, String, Float, Boolean

from app.api.db.database import Base


class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True, index=True)
    cadastral_number = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    result = Column(Boolean, nullable=True)
