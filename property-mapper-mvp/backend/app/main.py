import os
from fastapi import FastAPI, APIRouter, Request
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from app.property_mapper import property_mapper_router
from app.core.main_router import router as main_router
from app.core.logger import init_logging

load_dotenv(".env")

root_router = APIRouter()

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)
app.include_router(property_mapper_router)
app.include_router(root_router)

init_logging()

if __name__ == "__main__":
   
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
