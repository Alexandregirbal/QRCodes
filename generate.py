import os

import qrcode
from PIL import Image

from config import OUTPUT_FOLDER


def generate_qrcode(
    url: str, pixel_color: str, background_color: str, size: int, output_file: str
) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size // 25,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=pixel_color, back_color=background_color)

    qr_img.save(os.path.join(OUTPUT_FOLDER, output_file))
