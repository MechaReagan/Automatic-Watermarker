import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

watermark = Image.open("watermark.png")
watermark = watermark.resize((100, 100))
watermark_width, watermark_height = watermark.size

upload_icon = Image.open("upload-image-icon.png")
upload_icon = upload_icon.resize((200, 200))

window = tk.Tk()
window.title("Automatic Watermarker")
window.config(background="#FFD700")
window.geometry("600x600")

upload_window = tk.Frame(window, bg="#F5F5F5", cursor="target")
upload_window.place(height=500, width=500, x=300, y=260, anchor="center")


def upload():
    global img, image, label, resized_image
    try:
        label.destroy()
    except:
        pass
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    image = ImageTk.getimage(img)
    x, y = image.size
    if x >= y:
        y = int(500 * (y / x))
        x = 500
    elif y >= x:
        y = 500
        x = int(500 * (y / x))
    resized_image = image.resize(size=(x, y))
    img = ImageTk.PhotoImage(resized_image)
    label = tk.Label(upload_window, image=img)
    label.pack()


def watermark_img():
    global img, image, label
    if img:
        x, y = image.size
        margin = 40
        position_br = (x - margin - watermark_width, y - margin - watermark_height)
        image.paste(watermark, position_br, watermark)
        if x >= y:
            y = int(500 * (y / x))
            x = 500
        elif y >= x:
            y = 500
            x = int(500 * (y / x))
        resized_image = image.resize(size=(x, y))
        resized_image.paste(watermark, position_br, watermark)
        img = ImageTk.PhotoImage(resized_image)
        label.destroy()
        label = tk.Label(upload_window, image=img)
        label.pack()
    else:
        pass


def download():
    global image
    image = image.save("watermarked_img.png")
    confirmation = tk.Label(window, text="The watermarked image has been saved successfully!", background="#FFD700",
                            font=("Arial", 14))
    confirmation.place(x=300, y=580, anchor="center")
    confirmation.after(4000, confirmation.destroy)


upload_button = tk.Button(text="Upload", command=upload)
upload_button.place(x=50, y=540, height=40, width=80, anchor="w")

watermark_button = tk.Button(text="Watermark it!", command=watermark_img)
watermark_button.place(x=300, y=540, height=40, width=80, anchor="center")

download_button = tk.Button(text="Download", command=download)
download_button.place(x=550, y=540, height=40, width=80, anchor="e")

upload_icon = ImageTk.PhotoImage(upload_icon)
label = tk.Label(upload_window, image=upload_icon)
label.place(x=150, y=150)

window.mainloop()
