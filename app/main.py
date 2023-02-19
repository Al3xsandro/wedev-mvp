from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import routes

app = FastAPI(
    title="Wedev Software",
    description="API responsável por gerenciar a escola de programação proposta pelo desafio",
    version=1.0,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(routes)
