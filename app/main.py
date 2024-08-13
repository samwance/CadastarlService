from fastapi import FastAPI

from app.api.core.config import settings
from app.api.db.database import Base, engine
from app.api.endpoints import query, result, history, ping, auth, admin
from app.api.utils.csu import create_superuser_if_not_exists

app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(query.router, tags=["query"])
app.include_router(result.router, tags=["result"])
app.include_router(history.router, tags=["history"])
app.include_router(ping.router, tags=["ping"])
app.include_router(auth.router, tags=["auth"])
app.include_router(admin.router, tags=["admin"])


@app.on_event("startup")
async def startup_event():
    pass
