from PIL import Image
from config import ROOTPATH


def generate_qrcode(
    url: str, pixel_color: str, background_color: str, size: int, output_file: str
) -> None:
    # create new image with specified size and background color
    img = Image.new("RGB", (size, size), color=background_color)

    # load pixel color from url
    try:
        pixel = Image.open(url).convert("RGB")
    except:
        raise ValueError("Invalid url provided.")

    # resize pixel image to match specified size
    pixel = pixel.resize((size, size))

    # add pixel image to main image
    for x in range(size):
        for y in range(size):
            img.putpixel((x, y), pixel.getpixel((x, y)))

    # save final image to output file
    img.save(os.path.join(ROOTPATH, output_file))
