import socket
import tkinter as tk
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
window=tk.Tk()
host_entry = tk.Entry(fg="yellow", bg="blue", width=50)
port_entry=tk.Entry(fg="yellow", bg="blue", width=50)
host_entry.pack()
port_entry.pack()
HOST=host_entry.get()
PORT=port_entry.get()
host_label=tk.Label(text=HOST)
port_label=tk.Label(text=PORT)
host_label.pack()
port_label.pack()
window.mainloop()