import socket
import tkinter as tk
from tkinter.filedialog import askopenfilename
HOST,PORT=0,0
sock=''
flag=False
filepath=''
def connect():
    global HOST
    global PORT
    global sock
    global error_label
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, int(PORT)))
        error_label['text'] = 'соединение установлено'
    except:
        error_label['text']='ошибка соединения'
        pass

def send_picture():
    global error_label
    global flag
    if flag:
        connect()
        flag = False
    img=open(filepath,'rb+')
    while True:
        data=img.readline(2048)
        if not data:
            sock.send(data)
            break
        sock.send(data)
    error_label['text']='отправлено'
    img.close()
    sock.close()
    flag=True
    print(flag)

def break_connection():
    global sock
    sock.close()
def take_server_data():
    global HOST
    global PORT
    HOST=host_entry.get()
    PORT=port_entry.get()
    connect()
def open_file():
    global filepath
    filepath = askopenfilename(filetypes=[("All Files", "*.*")])
    send_picture()
window=tk.Tk()
frame_input=tk.Frame(master=window)
button=tk.Frame(master=window)
file_input=tk.Frame(master=window)
host_label=tk.Label(master=frame_input,text="введите адрес")
host_entry = tk.Entry(master=frame_input,fg="black", bg="white", width=50)
port_label=tk.Label(master=frame_input,text="введите порт")
port_entry=tk.Entry(master=frame_input,fg="black", bg="white", width=50)
error_label=tk.Label(master=frame_input,text="")
host_label.pack()
host_entry.pack()
port_label.pack()
port_entry.pack()
error_label.pack()
frame_input.pack(side=tk.LEFT,expand=True)
apply_button=tk.Button(master=button,text="Подключиться", command=take_server_data)
apply_button.pack()
decline_button=tk.Button(master=button,text="Отключиться", command=break_connection)
decline_button.pack()
button.pack(side=tk.LEFT,expand=True)
file_button=tk.Button(master=button,text="выбрать файл", command=open_file)
file_button.pack()
window.mainloop()