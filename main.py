import os
from PIL import Image, ImageDraw


text = """
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
"""


def draw_img(text):
    img = Image.new("RGBA", (8, 8))

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 0, 0], fill="red")

    img.save("out/out.png")


def convert_string_to_array(string):
    arr = [row.split(" ") for row in string.strip().split("\n")]
    return arr


def draw_one_pixel(string, draw_ins, width, height):
    pass


draw_img("text")
