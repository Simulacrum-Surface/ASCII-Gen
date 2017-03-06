#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""

Name: [I have no clue]
Autor: Simulacrum
License: WTFPL
Version: 1.0.0.0

"""

from PIL import Image
import optparse


def read_params():
    reader = optparse.OptionParser()
    reader.add_option("-s", "--size", action="store", type="int", dest="size", help="Define a line-length of characters used to display the image-width")
    (option, path) = reader.parse_args()
    return (option, path)

def img_size(path, *wantedX):
    try:
        file = Image.open(path)
        new_color_scheme = file.convert("RGB")
        point = new_color_scheme.load()
        x, y = file.size
        return (x, y, point)



    except:
        print("[-] Looks like this is not a picture...\nExiting.")
        exit(0)


def main(params):
    #extract the params
    option, path = params
    if len(path) == 1:
        x, y, point = img_size(path[0])

        # This is a dict. I know it could be a list. -> planned features need dict.
        char_map = {0: "#", 1: "M", 2: "@", 3: "%",
                    4: "!", 5: "=", 6: "+", 7: "~",
                    8: ":", 9: "-", 10: ",",
                    11: ".", 12: " "}

        art_string = ""

        # Iterating though the pixels.
        for cordy in range(0, y):
            for cordx in range(0, x):
                r, g, b = point[cordx, cordy]
                # Give the colors a different emphasis and calculate the luma. Used: Digital ITU BT.601
                pixel_luma = round(((0.299 * r + 0.587 * g + 0.114 * b) / 255) * 10, 0)
                if pixel_luma in char_map:
                    art_string = art_string + char_map[pixel_luma]
                else:
                    # What a useful error msg :)
                    print("[-] Something went horribly wrong.\nExiting...")
                    exit(0)
        art_list = list(art_string)
        new_x = x
        # Format the output string(list)
        for lines in range(0, y):
            art_list.insert(new_x, "\n")
            new_x = new_x + x + 1
        art_string = "".join(art_list)
        print(art_string)
    else:
        print("[-] Please specify ONE picture.\nExiting...")
        exit(0)

    return


if __name__ == '__main__':
    params = read_params()
    main(params=params)
