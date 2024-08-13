from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api.db.database import get_db
from app.api.db.models.user import User
from app.api.schemas.user import UserCreate, UserResponse
from app.api.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter()


async def get_user_by_username(username: str, db: AsyncSession):
    """Функция для поиска пользователя по имени пользователя"""
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_username(user.username, db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    if len(user.password) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 2 characters long :)"
        )

    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@router.post("/login")
async def login(
    username: str = Body(...),
    password: str = Body(...),
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_username(username, db)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(password, user.hashed_password):
        print(password, user.hashed_password)
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}