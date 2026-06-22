from PIL import Image
import sys


def main():
    images = []
    for arg in sys.argv[1:]:
        images.append(Image.open(arg))
    images[0].save(
        "pillow.gif", save_all=True, append=[images[1]], duration=200, loop=0
    )


if __name__ == "__main__":
    main()
