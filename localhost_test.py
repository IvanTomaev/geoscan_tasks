import socket
import threading
import tkinter as tk
from PIL import ImageTk, Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
window=''
def update():
    global panel
    print(panel)
    img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
    v = ImageTk.PhotoImage(img)
    panel.config(image=v)
    panel.image=v
    img.close()
    window.after(1000, update)
def draw():
    global panel
    global window
    window = tk.Tk()
    img = Image.open(r'C:\Users\Computer\Desktop\image.jpg')
    v = ImageTk.PhotoImage(img)
    panel = tk.Label(image=v)
    print(panel)
    panel.pack()
    img.close()
    window.after(1000,update)
    window.mainloop()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
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
    data = conn.recv(512)
    if not data:
        print('received')
        file.close()
        flag=True
        if n:
            my_thread.start()
            n=not n
    else:
        file.write(data)








