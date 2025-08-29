from fastapi import FastAPI

from qr_code_generation.api import qr_routes

app = FastAPI(
    title="QR Code Generator API",
    version="1.0.0",
    description="API simples para gerar QR Codes a partir de URLs.",
)

app.include_router(qr_routes.router, prefix="/api/v1/qr", tags=["QR Code"])
