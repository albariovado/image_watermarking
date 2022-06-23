import tkinter as tk
from var import *
from fun import *
from PIL import Image

# ----------------------------  UI SETUP    ------------------------------- #

window = tk.Tk()
window.title("Image Watermarking")
window.config(padx=100, pady=50, bg=BG_COLOR_HEX)

# ----------------------------  LABELS      ------------------------------- #

title = tk.Label(text='Image Watermarking',fg=TITLE_COLOR, font=TITLE_FONT, bg=BG_COLOR_HEX)
title.grid(column=0,row=0,columnspan=2)

info = tk.Label(text='You\'ll find your image saved as "output.jpg" in the same directory where this program ran.',fg=INFO_COLOR, font=INFO_FONT, bg=BG_COLOR_HEX)
info.grid(column=0,row=6,columnspan=2)

# preview = tk.Label(text='Preview:',fg=PREVIEW_COLOR, font=PREVIEW_FONT, bg=BG_COLOR_HEX)
# preview.grid(column=0,row=3)

# ----------------------------  CANVAS      ------------------------------- #

# canvas = tk.Canvas(width=600, height=600, bg=BG_COLOR_HEX, highlightthickness=0)
# preview_img = tk.PhotoImage(file='output.jpg')
# canvas.create_image(300, 300, image=preview_img)
# canvas.grid(column=0,row=4,columnspan=2)

# ----------------------------  BUTTONS     ------------------------------- #

select_img = tk.Button(text="select image", command=select_image, highlightthickness=0)
select_img.grid(column=0,row=1)

select_wtrmk = tk.Button(text="select watermark", command=select_watermark, highlightthickness=0)
select_wtrmk.grid(column=1,row=1)

show_prev = tk.Button(text="show preview", command=show_preview, highlightthickness=0)
show_prev.grid(column=0,row=2,columnspan=2)

save_img = tk.Button(text="save", command=save_image, highlightthickness=0)
save_img.grid(column=0,row=5,columnspan=2)

# ----------------------------  MAINLOOP     ------------------------------- #

window.mainloop()