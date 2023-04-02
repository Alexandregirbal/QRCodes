from generate import generate_qrcode, image_to_pdf

if __name__ == "__main__":
    sizes = [5, 8, 10, 15, 20]
    for size in sizes:
        qr_size = size * 25
        qrcode_image = generate_qrcode(
            url="https://alexandre-girbal.notion.site/Le-Clos-des-Mimosas-62f8e60f647348e88c8d1973d8bffbf9",
            pixel_color="#000000",
            background_color="#ffffff",
            size=qr_size,
            output_file=f"LeClosDesMimosas_{size}.png",
        )

        image_to_pdf(image_path=qrcode_image, qr_size=qr_size, size=size)
