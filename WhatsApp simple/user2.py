import socket
import tkinter
from tkinter import simpledialog
import threading


HOST = "127.0.0.1"
PORT = 9090

client = socket.create_connection((HOST, PORT))


def push():
    data = message.get()
    client.send(bytes(data, "UTF-8"))
    message.delete(0, tkinter.END)


def input():
    while True:
        message_server = client.recv(1024).decode("UTF-8")
        text = f"{data.get('1.0', tkinter.END).strip()}\n{message_server}"
        print(text)
        data.delete("1.0", tkinter.END)
        data.insert("1.0", text)


# Отправляем имя пользователя
nickname = simpledialog.askstring("Nickname", "Please choose a nickname")
client.send(bytes(nickname, "UTF-8"))

# Создаем виртуальную среду
root = tkinter.Tk()
# Окно для текста
data = tkinter.Text(root, bd=10)
data.grid(row=0, column=0, columnspan=2)

# консоль для сообщения
message = tkinter.Entry(root, width=50, font=("Arial", 15), bd=10)
message.grid(row=1, column=0)

# Кнопка
click = tkinter.Button(root, text="Отправить", font=("Arial", 10), bd=10, command=push)
click.grid(row=1, column=1)

root.grid_columnconfigure(100)
root.grid_columnconfigure(100)

# Многопоточность
tk = threading.Thread(target=input)
tk.start()

root.mainloop()
