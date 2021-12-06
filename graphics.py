import tkinter as tk
from PIL import ImageTk, Image, ImageFile
import sys
ImageFile.LOAD_TRUNCATED_IMAGES = True
def update():
    global panel
    img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
    img = img.resize((640, 480), Image.ANTIALIAS)
    v = ImageTk.PhotoImage(img)
    panel.config(image=v)
    panel.image=v
    img.close()
    window.after(500, update)
def init():


window = tk.Tk()
frame=tk.Frame()
port_label=tk.Label(master=frame,text='Введите порт')
button=tk.Button(master=frame,text='Запустить сервер', command=init)
img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
img = img.resize((640, 480), Image.ANTIALIAS)
v = ImageTk.PhotoImage(img)
panel = tk.Label(image=v)
panel.pack()
img.close()
window.after(1000,update)
window.mainloop()