import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFilter
from var import *

img_path = ''
wtrmk_path = ''

result = None

def select_image():
    tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    global img_path
    img_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return

def select_watermark():
    tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    global wtrmk_path
    wtrmk_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return

def show_preview():
    global result
    img = Image.open(img_path)
    wtrmk = Image.open(wtrmk_path)
    img.paste(wtrmk)
    img.show()
    result = img
    return

def save_image():
    result.save('output.jpg')
    return