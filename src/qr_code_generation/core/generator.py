import qrcode
from PIL import Image


def generate_qr(data: str) -> Image.Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


if __name__ == "__main__":
    breakpoint()
    img = generate_qr("mandacarumercado.com.br")
    img.save("test_qr.png")
    # img.show()
