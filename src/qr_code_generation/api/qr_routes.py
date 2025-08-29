from io import BytesIO

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, HttpUrl

from qr_code_generation.core.generator import generate_qr

router = APIRouter()


class QRRequest(BaseModel):
    url: HttpUrl


@router.post("/generate", summary="Gerar QR Code", response_description="Imagem PNG")
def generate(req: QRRequest):
    if not req.url:
        raise HTTPException(status_code=400, detail="url is required")

    img = generate_qr(str(req.url))
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
