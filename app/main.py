from fastapi import FastAPI
from app.home.views import router as home_router

app = FastAPI(
    title="FastAPI GraphQL",
    description="Welcome to FastAPI GraphQL project documentation!",
    root_path="/",
    docs_url='/docs',
    openapi_url="/docs/openapi.json",
    redoc_url="/redoc"
)


app.include_router(home_router, prefix="/home", tags=["home"])
