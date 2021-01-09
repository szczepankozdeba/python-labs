#!/usr/bin/python3

from PIL import Image

im = Image.open('krzys.jpg')
im.save('krzys.png')

im = Image.open('magda.jpg')
im.save('magda.png')

im = Image.open('maryla.jpg')
im.save('maryla.png')

im = Image.open('robert.jpg')
im.save('robert.png')