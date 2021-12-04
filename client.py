import socket
import tkinter as tk
from tkinter.filedialog import askopenfilename
HOST,PORT=0,0
sock = socket.socket()
filepath=''
def connect(HOST,PORT):
    global sock
    global error_label
    try:
        sock.connect((HOST, int(PORT)))

    except:
        error_label['text']='ошибка соединения'
        pass
    error_label['text'] = ''
    send_picture()
def send_picture():
    img=open(filepath,'rb+')
    data=''
    while True:
        data=img.readline(512)
        if not data:
            break
        sock.send(data)

def break_connection():
    global sock
    sock.close()
def take_server_data():
    global HOST
    global PORT
    HOST=host_entry.get()
    PORT=port_entry.get()
    connect(HOST,PORT)
def open_file():
    global filepath
    filepath = askopenfilename(filetypes=[("All Files", "*.*")])
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