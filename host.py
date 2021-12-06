import socket
import threading
import tkinter as tk
from PIL import ImageTk, Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
window=''
def update():
    global panel
    img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
    img = img.resize((640, 480), Image.ANTIALIAS)
    v = ImageTk.PhotoImage(img)
    panel.config(image=v)
    panel.image=v
    img.close()
    window.after(500, update)
def draw():
    global panel
    global window
    window = tk.Tk()
    img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
    img = img.resize((640, 480), Image.ANTIALIAS)
    v = ImageTk.PhotoImage(img)
    panel = tk.Label(image=v)
    panel.pack()
    img.close()
    window.after(1000,update)
    window.mainloop()

def prog(PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', PORT))
    print('binded')
    sock.listen(1)
    conn, addr = sock.accept()
    my_thread = threading.Thread(target=draw)
    n=True
    file=open(r'C:\Users\Computer\Desktop\image.jpg','wb')
    print ('connected:', addr)
    flag=False
    while True:
        if flag:
            conn, addr = sock.accept()
            file = open(r'C:\Users\Computer\Desktop\image.jpg', 'wb')
            flag=False
        data = conn.recv(2048)
        if not data:
            print('received')
            file.close()
            flag=True
            if n:
                my_thread.start()
                n=not n
        else:
            file.write(data)
def send():
    global window2
    global port_entry
    global port_entry
    PORT=int(port_entry.get())
    window2.destroy()
    prog(PORT)

def init():
    global port_entry
    global window2
    window2 = tk.Tk()
    label = tk.Label(master=window2,text='Введите порт')
    port_entry = tk.Entry(master=window2,fg="black", bg="white", width=50)
    button = tk.Button(master=window2,text="Запустить сервер", command=send)
    label.pack()
    port_entry.pack()
    button.pack()
    window2.mainloop()
port_entry=''
window2=''
thread=threading.Thread(target=init)
thread.start()


