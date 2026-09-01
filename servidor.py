import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0", 5000))
servidor.listen()

conexao, endereco = servidor.accept()

mensagem = conexao.recv(1024)
print(mensagem.decode())

conexao.send("Olá, cliente!".encode())

conexao.close()
servidor.close()
