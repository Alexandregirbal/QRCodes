from generate import generate_qrcode, image_to_pdf

if __name__ == "__main__":
    qrcode_image = generate_qrcode(
        url="https://www.notion.so/alexandre-girbal/Le-Clos-des-Mimosas-62f8e60f647348e88c8d1973d8bffbf9",
        pixel_color="#000000",
        background_color="#ffffff",
        size=100,
        output_file="LeClosDesMimosas.png",
    )

    image_to_pdf(image_path=qrcode_image, size=12)
