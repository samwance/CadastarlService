from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api.db.database import get_db
from app.api.db.models.query import Query
from app.api.schemas.query import QueryResponse

router = APIRouter()


@router.get("/history", response_model=list[QueryResponse])
async def get_history(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Query))
    return result.scalars().all()


@router.get("/history/{cadastral_number}/", response_model=list[QueryResponse])
async def get_history_by_cadastral_number(cadastral_number: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Query).where(Query.cadastral_number == cadastral_number))
    queries = result.scalars().all()

    if not queries:
        raise HTTPException(status_code=404, detail="Cadastral number not found")

    return queries
