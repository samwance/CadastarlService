from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db.database import get_db
from app.api.db.models.query import Query
from app.api.schemas.query import QueryCreate, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def create_query(query: QueryCreate, db: AsyncSession = Depends(get_db)):
    new_query = Query(
        cadastral_number=query.cadastral_number,
        latitude=query.latitude,
        longitude=query.longitude,
        result=False
    )
    db.add(new_query)
    await db.commit()
    await db.refresh(new_query)
    return new_query
