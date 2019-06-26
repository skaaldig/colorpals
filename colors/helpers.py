from PIL import Image
from matplotlib.colors import rgb2hex

COLORPALETTE_FIELD_NAMES = [
    "one", "two",
    "three", "four",
    "five", "six",
    "seven", "eight",
    "nine", "ten"
]

def stringify_rgb(rgb):
    """Used to convert rgb to string for saving in db"""
    rgb_value = f"{rgb[0]}, {rgb[1]}, {rgb[2]}, {rgb[3]}"
    return rgb_value


def stringify_hex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(rgb[0], rgb[1], rgb[2])


def sort_colors(colors):
    sorted_list = [n for n in range(len(colors))]
    counts = [count[0] for count in colors]
    counts.sort(reverse=True)
    order = [(pos, rank) for pos, rank in enumerate(counts)]

    for count, rgb in colors:
        for pos, rank in order:
            if count == rank:
                sorted_list[pos] = stringify_hex(rgb)

    return sorted_list


def get_colors(infile, numcolors=10):
    image = Image.open(infile)
    small_image = image.resize((80, 80))
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors).convert("RGB")  # image with only 10 dominating colors
    result.putalpha(0)
    colors = result.getcolors(80*80) # array of colors in the image
    colors = sort_colors(colors)
    return colors
