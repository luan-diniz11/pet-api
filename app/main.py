# Arquivo principal da aplicação
# FastAPI

from fastapi import FastAPI
from app.core.config import Settings 
from app.routers import health
app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.APP_VERSION
)

app.include_routers(health.router)