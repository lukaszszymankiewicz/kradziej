from cairosvg import svg2png

import os


def make_folder(name) -> None:
    try:
        os.mkdir(name)
    except FileExistsError:
        raise ValueError("Folder with song already exist. Please clean up current directory")


def save_svg_image_to_png(image, path):
    svg2png(bytestring=image, write_to=path)


def save_png_image(image, path):
    with open(path, "wb") as file:
        file.write(image)
