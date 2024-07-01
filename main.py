from fastapi import FastAPI
from sqlmodel import SQLModel
from dotenv import load_dotenv
from routers.products import router as products_router
load_dotenv()
from config import engine

SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def home():
    return "FastAPI Application"

app.include_router(products_router, prefix="/api/v1")
