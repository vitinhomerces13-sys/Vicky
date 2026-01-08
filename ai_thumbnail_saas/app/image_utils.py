from PIL import Image,ImageDraw,ImageFont
from config import FONT_PATH,IMAGE_W,IMAGE_H

def text_overlay(inp,txt,out):
    i=Image.open(inp).resize((IMAGE_W,IMAGE_H))
    d=ImageDraw.Draw(i)
    f=ImageFont.truetype(FONT_PATH,90)
    d.text((50,300),txt,font=f,fill="yellow",stroke_width=4,stroke_fill="black")
    i.save(out)
