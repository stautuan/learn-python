"""
Implement a program that expects exactly two command-line arguments:
    - in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    - in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
sys.exit():
    - if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
    - if the input’s name does not have the same extension as the output’s name
"""
# TODO: organize code 

import os
import sys

from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

# first, filter the extensions that ends with ".jpg", ".jpeg", ".png"
if not (file_path1.lower().endswith((".jpg", ".jpeg", ".png")) and file_path2.lower().endswith((".jpg", ".jpeg", ".png"))):
    sys.exit("Invalid output")

# check if both extensions are the same using splitext
ext = os.path.splitext(file_path1.lower())
if not file_path2.lower().endswith(ext[1]):
    sys.exit("Input and output have different extensions")


try:
    # open input with Image.open()
    with Image.open(file_path1) as muppet, Image.open("shirt.png") as shirt:

        # resize and crop the input with ImageOps.fit()
        muppet = ImageOps.fit(muppet, shirt.size)

        # overlay shirt with Image.paste()
        muppet.paste(shirt, shirt)

        # save the result
        muppet.save(file_path2)

except FileNotFoundError:
    sys.exit("Input does not exist")
