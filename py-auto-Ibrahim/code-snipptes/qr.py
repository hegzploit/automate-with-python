#!/usr/bin/python3
import os
import qrcode

img = qrcode.make("https://aboueleyes.me")
img.save("blog.png", "PNG")
os.system('feh blog.png')
