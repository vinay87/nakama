# -*- coding: utf-8 -*-
import os

from epd import epd2in7b
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#import imagedata

COLORED = 1
UNCOLORED = 0

def run():
    from nakama import get_op_stat_image
    img_b, img_r = get_op_stat_image()
    img_b = img_b.transpose(Image.ROTATE_90)
    img_r = img_r.transpose(Image.ROTATE_90)
    epd = epd2in7b.EPD()
    epd.init()
    # # clear the frame buffer
    # frame_black = [0] * (epd.width * epd.height / 8)
    # frame_red = [0] * (epd.width * epd.height / 8)

    frame_black = epd.get_frame_buffer(img_b)
    frame_red = epd.get_frame_buffer(img_r)
    epd.display_frame(frame_black, frame_red)

    #os.remove("black.bmp")
    #os.remove("red.bmp")
    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_RED)

if __name__ == "__main__":
    run()
