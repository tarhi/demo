
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.main import api_router
from app.core.config import settings


app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/", include_in_schema=False)  
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
