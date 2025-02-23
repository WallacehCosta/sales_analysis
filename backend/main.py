from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import sales_routes, user_routes

app = FastAPI(title="Sales Analyzer API", version="1.0.0")

# Configuração do CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (ajuste para produção)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas
app.include_router(sales_routes.router, prefix="/api/sales", tags=["sales"])
app.include_router(user_routes.router, prefix="/api/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sales Analyzer API!"}
