import socket
import threading


HOST = "127.0.0.1"
PORT = 9090

server = socket.create_server((HOST, PORT))
server.listen()

# Информация о пользователях
clients = []
nicknames = []


def push(message):
    for client in clients:
        print("Информация о клиенте", client)
        print(message)
        client.send(bytes(message, "UTF-8"))


def input_message(client):
    while True:
        message = client.recv(1024).decode("UTF-8")
        print(message)
        push(f"{nicknames[clients.index(client)]}: {message}")


def main():
    while True:
        client, address = server.accept()

        # Принимаем информацию о пользователе
        clients.append(client)

        name = client.recv(1024).decode("UTF-8")
        nicknames.append(name)

        # Создаем поток
        tk = threading.Thread(target=input_message, args=(client,))

        tk.start()





print("Сервер работает...")
main()
