import random
import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.db.database import get_db
from app.api.db.models.query import Query
from app.api.utils.external_service import ExternalService

router = APIRouter()

router = APIRouter()

@router.post("/result/{query_id}/")
async def process_result(query_id: int, db: AsyncSession = Depends(get_db)):
    query = await db.get(Query, query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    # Эмулирует отправку запроса на внешний сервер
    query.result = await ExternalService.simulate_request()

    await db.commit()
    await db.refresh(query)
    return {"id": query.id, "cadastral": query.cadastral_number, "result": query.result}
