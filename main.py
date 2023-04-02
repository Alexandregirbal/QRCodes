from generate import generate_qrcode

if __name__ == "__main__":
    generate_qrcode(
        url="https://www.notion.so/alexandre-girbal/Le-Clos-des-Mimosas-62f8e60f647348e88c8d1973d8bffbf9",
        pixel_color="#000000",
        background_color="#ffffff",
        size=100,
        output_file="LeClosDesMimosas.png",
    )
