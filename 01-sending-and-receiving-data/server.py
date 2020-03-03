import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), nomor port bebas asal tidak kurang dari 1234))
s.bind((socket.gethostname(), 2000))
# s.listen(respon max jika terlalu banyak request yang menumpuk)
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    clientsocket.close()
