# coding: utf-8

import sys
import optparse
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FONT_DEFAULT = "./Baloo-Regular.ttf"
STRING_DEFAULT = "LGTM!"
OUT_DEFAULT = 'LGTM.jpeg'

parser = optparse.OptionParser()
parser.add_option('-s', action="store", default=60, type="int")
parser.add_option('-x', action="store", default=10, type="int")
parser.add_option('-y', action="store", default=10, type="int") 
parser.add_option('-c', action="store", default="#FFFFFF")
parser.add_option('-f', action="store", default=FONT_DEFAULT)
parser.add_option('-t', action="store", default=STRING_DEFAULT)
parser.add_option('-o', action="store", default=OUT_DEFAULT)

def main():
  options, args = parser.parse_args()
  fonr_size = options.s
  x = options.x
  y = options.y
  color = options.c
  font = options.f
  text = options.t
  out = options.o

  #　画像の読み込み
  img = Image.open(args[0])
  print('Image Size :', img.size)
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype(font, fonr_size, encoding='utf-8')
  draw.text((x,y), text, font=font, fill=color)
  img.save(out)

if __name__ == "__main__":
  main();
