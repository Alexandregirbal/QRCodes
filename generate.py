import os

import qrcode
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

    output_file = os.path.join(OUTPUT_FOLDER, output_file)
    qr_img.save(output_file)
    return output_file


def image_to_pdf(image_path: str, size: float, title: str) -> None:
    """Converts an image to a PDF file
    - image_path: path to the image to convert
    - size: size of the image in cm
    - title: title of the PDF file
    """
    image = Image.open(image_path)
    width, height = image.size

    # convert cm to points (1 cm = 28.35 points)
    size = size * 28.35

    # calculate the position and size of the image in the PDF
    x = (letter[0] - size) / 2
    y = (letter[1] - size) / 2
    aspect_ratio = width / float(height)
    if aspect_ratio > 1:
        pdf_width = size
        pdf_height = size / aspect_ratio
    else:
        pdf_width = size * aspect_ratio
        pdf_height = size

    # create new PDF canvas and embed the image in it
    pdf_file = f"{image_path.split('.')[0]}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setTitle(title)
    c.drawImage(image_path, x, y, width=pdf_width, height=pdf_height)
    c.save()
