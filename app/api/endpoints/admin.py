from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api.db.database import get_db
from app.api.db.models.user import User
from app.api.schemas.user import UserResponse
from app.api.core.security import get_current_active_superuser

router = APIRouter()


@router.get("/admin/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    result = await db.execute(select(User))
    return result.scalars().all()
