import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.namahostserver(), nomor port server))
s.connect((socket.gethostname(), 2000))
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break

    full_msg += msg.decode("utf-8")

print(full_msg)