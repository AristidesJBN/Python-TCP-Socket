import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("172.16.1.7", 5000))

cliente.send("Olá, servidor!".encode())

mensagem = cliente.recv(1024)
print(mensagem.decode())

cliente.close()
