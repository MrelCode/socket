import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.namahostserver(), nomor port server))
s.connect((socket.gethostname(), 2000))

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(31)
        if new_msg:
            print(f"new message length: {HEADERSIZE}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full message recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg)