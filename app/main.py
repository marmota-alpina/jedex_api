from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    description="Jedex API",
    version="1.0.0",
    title="Jedex API",
    redoc_url="/jedex/redoc",
    docs_url="/jedex",
    openapi_url="/jedex/openapi.json"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
app.include_router(api_router, prefix="/jedex/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to Jedex API"}
