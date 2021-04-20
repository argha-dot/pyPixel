from PIL import Image, ImageDraw, ImageColor

text = """
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 3 3 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 3 3 6 3 3 5 5 3 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 5 3 6 3 6 3 3 5 5 6 3 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 5 3 6 6 3 6 3 3 5 5 6 6 3 5 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 5 5 6 6 3 6 3 3 5 5 6 6 5 5 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 5 5 5 3 6 3 6 3 3 5 5 6 3 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 5 5 5 6 3 3 6 3 3 5 5 3 6 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 5 5 6 3 3 3 6 3 3 5 5 3 3 6 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 5 3 3 1 1 1 3 5 5 3 1 1 1 3 3 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 5 3 1 1 1 1 1 3 3 1 1 1 1 1 3 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 3 1 1 4 3 4 1 5 5 1 3 4 4 1 1 3 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 3 1 1 1 4 4 4 1 3 3 1 4 4 4 1 1 1 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 3 1 1 5 3 3 3 3 1 1 3 3 3 3 5 1 1 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 3 1 1 1 5 5 5 5 3 1 1 3 5 5 5 5 1 1 1 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 3 1 1 1 5 5 5 3 1 1 1 1 3 5 5 5 1 1 1 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3 1 1 1 1 1 5 5 1 5 1 5 1 1 3 5 1 1 1 1 1 3 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 1 6 1 1 5 1 5 1 5 1 6 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 3 3 5 5 1 1 1 1 5 5 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 3 3 5 5 5 5 1 1 1 5 5 5 5 1 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 5 5 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 1 5 5 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 5 5 1 1 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 1 1 5 5 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 1 3 1 3 5 3 3 5 5 3 3 5 5 3 3 5 5 3 1 3 1 5 5 0 0 0 0 0 0 0
0 0 0 0 0 0 5 5 1 3 3 1 3 5 3 3 5 5 3 3 5 5 3 3 5 5 3 1 3 3 1 5 5 0 0 0 0 0 0
0 0 0 0 0 5 5 1 1 1 1 1 3 5 3 3 5 5 3 3 5 5 3 3 5 5 3 1 1 1 1 1 5 5 0 0 0 0 0
0 0 0 0 5 5 5 1 5 5 1 1 1 1 3 3 5 5 3 3 5 5 3 3 1 1 1 1 5 5 5 1 5 5 5 0 0 0 0
0 0 0 5 5 5 1 5 5 5 1 1 1 5 1 1 5 5 3 3 5 5 1 1 1 5 1 1 1 5 5 5 1 5 5 5 0 0 0
0 0 0 5 5 1 5 5 5 1 1 1 5 5 5 1 1 1 3 3 1 1 1 5 5 5 1 1 1 1 5 5 5 1 5 5 0 0 0
0 0 5 5 5 1 5 5 1 1 1 1 5 5 5 1 3 3 1 1 3 3 5 5 5 5 1 1 1 1 1 5 5 1 5 5 5 0 0
0 0 5 5 5 1 5 1 1 1 1 1 5 5 5 1 1 1 1 1 1 1 5 1 5 5 1 1 1 1 1 1 5 1 5 5 5 0 0
0 5 5 5 5 1 5 1 1 1 1 1 5 1 5 1 1 3 3 1 7 1 5 1 5 5 1 1 1 1 1 1 5 1 5 5 5 5 0
0 5 5 5 5 1 5 3 1 1 1 1 5 1 5 1 1 1 1 1 1 1 5 1 5 5 1 1 1 1 1 3 5 1 5 5 5 5 0
0 5 5 5 5 1 3 5 3 1 1 1 5 1 5 1 1 3 3 1 8 1 5 1 5 5 1 1 1 1 3 5 3 1 5 5 5 5 0
0 5 5 5 5 1 5 3 5 3 1 1 5 1 5 1 1 1 1 1 1 1 5 1 5 5 1 1 1 3 5 3 5 1 5 5 5 5 0
0 5 5 5 5 1 5 5 3 5 3 1 5 1 5 1 3 3 3 3 3 3 1 1 5 5 1 1 3 5 3 5 5 1 5 5 5 5 0
0 5 5 5 5 1 1 5 5 3 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 3 5 5 1 1 5 5 5 5 0
0 5 5 5 5 1 1 1 5 5 5 1 3 1 9 1 1 3 3 3 3 1 1 9 1 3 1 1 5 5 5 1 1 1 5 5 5 5 0
0 5 5 5 5 1 1 1 1 5 1 1 1 1 1 1 1 5 5 3 3 1 1 1 1 1 1 1 1 5 1 1 1 1 5 5 5 5 0
0 5 5 5 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5 0
0 5 5 5 5 1 1 1 1 1 1 1 5 1 5 1 5 5 5 5 5 5 1 5 1 3 1 1 1 1 1 1 1 1 5 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 5 5 5 5 5 1 5 1 3 5 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 1 5 5 1 5 5 5 5 5 5 1 5 1 5 5 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 1 5 5 1 1 5 5 5 5 1 1 5 1 6 3 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 1 5 5 1 1 5 5 5 5 1 1 5 1 6 3 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 1 5 5 1 5 1 5 5 1 5 1 5 1 3 5 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 1 5 5 1 5 5 1 1 5 5 1 5 1 5 5 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 5 1 5 5 5 1 5 1 3 5 1 1 1 1 1 1 1 1 5 5 5 0
0 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 5 1 5 5 5 1 5 1 3 5 1 1 1 1 1 1 1 1 5 5 5 0
5 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 5 1 5 5 5 1 5 1 3 5 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 1 1 1 5 5 1 5 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 1 1 1 5 5 1 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 5 5 1 5 1 1 1 5 5 1 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 1 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 1 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 1 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 1 5 1 5 1 1 1 5 5 1 5 1 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 1 1 1 1 5 1 1 1 5 5 1 1 1 1 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 3 5 5 5 1 1 1 5 3 5 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 1 1 1 1 1 1 5 3 5 5 5 1 1 1 5 3 5 5 5 5 1 1 1 1 1 1 1 1 1 5 5 5 5
5 5 5 5 1 1 0 0 0 0 0 0 1 1 1 5 5 1 1 1 5 5 5 1 1 1 0 0 0 0 0 0 0 1 1 5 5 5 5
0 0 5 5 0 0 0 0 0 0 0 1 3 3 5 1 1 1 0 0 1 1 3 5 5 5 1 0 0 0 0 0 0 1 1 5 5 5 5
0 0 0 0 0 0 0 0 0 1 3 3 5 5 5 5 5 1 0 0 1 5 3 3 5 5 5 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 5 5 5 5 5 5 5 5 1 0 0 1 5 5 5 5 5 5 1 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 2 1 1 1 1 1 1 1 1 1 1 2 2 1 1 1 1 1 1 1 1 1 2 2 2 2 0 0 0 0 0 0
"""

colors = [
    "#1D191A",
    "#eaeaec",
    "#747474",
    "#453C35",
    "#343031",
    "#fff",
    "#fc3435",
    "#1F3A93",
    "#00943b",
]


def draw_img(text, zoom=1):
    arr = convert_string_to_array(text)

    res = [len(arr[0]), len(arr)]  # width, height

    img = Image.new("RGBA", res)

    d = ImageDraw.Draw(img)

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            draw_one_pixel(arr[y][x], d, x, y, colors)

    img = img.resize((res[0] * zoom, res[1] * zoom), resample=Image.NEAREST)
    img.save("out/out.png")


def convert_string_to_array(string):
    arr = [row.strip().split(" ") for row in string.strip().split("\n")]
    return arr


def draw_one_pixel(string, draw_ins, x, y, colors):
    int_str = int(string)

    color = []
    if int_str != 0:
        color = ImageColor.getrgb(colors[int_str - 1])
    else:
        color = 0

    if isinstance(colors, list):
        draw_ins.rectangle([x, y, x, y], fill=color)


draw_img(text, zoom=3)
