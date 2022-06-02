from PIL import Image, ImageDraw, ImageFont

font_title = "./develop_env/font3d/test_overloop.otf"
size_title = 40
im_new = Image.new(mode='RGB', size=(1280, 720), color=(0, 0, 0))
im_new.show()
d = ImageDraw.Draw(im_new)
fnt = ImageFont.truetype(font_title, size_title)
# Set height in top off image
title = "TOP ABCXYZ SONG HIT \n 2021"
color_title = (255, 255, 255)
space_line = 30

d.multiline_text((100, 100), text=title, font=fnt,
                 fill=color_title, align='center')
im_new.show()