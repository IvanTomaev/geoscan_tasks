import socket
import tkinter as tk
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.31.138', 9090))
print('binded')
sock.listen(1)
conn, addr = sock.accept()
file=open(r'C:\Users\Ольга Александровна\Desktop\image.jpg','wb+')
print ('connected:', addr)
window=tk.Tk()

while True:
    data = conn.recv(512)
    if not data:
        img=Image.open(r'C:\Users\Ольга Александровна\Desktop\image.jpg')
        img.pack()
        window.mainloop()
    else:
        file.write(data)


conn.close()
