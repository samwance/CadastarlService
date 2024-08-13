import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api.db.models.user import User
from app.api.core.security import get_password_hash


async def create_superuser_if_not_exists(db: AsyncSession, username: str, password: str):
    result = await db.execute(select(User).filter(User.username == username))
    user = result.scalar_one_or_none()

    if user is None:
        hashed_password = get_password_hash(password)
        new_user = User(username=username, hashed_password=hashed_password, is_superuser=True)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        logging.info(f"Superuser '{username}' created.")
    else:
        logging.info(f"Superuser '{username}' already exists.")