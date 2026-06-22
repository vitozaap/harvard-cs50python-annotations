import csv
import sys
from PIL import Image, ImageOps
import os


def main():
    shirt()


def shirt():
    allowed_ext = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].lower().endswith(allowed_ext) or not sys.argv[2].lower().endswith(allowed_ext):
        sys.exit("Invalid input")
    if os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
        sys.exit("Input and output have different extensions")

    shirt = Image.open("shirt.png")
    try:
        image = ImageOps.fit(Image.open(sys.argv[1].lower()), size=shirt.size)

        image.paste(shirt, mask=shirt.convert("RGBA"))
        image.save(sys.argv[2].lower())
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
