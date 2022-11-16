import socket
hn=socket.gethostname()
ipadd=socket.gethostbyname(hn)
print(ipadd)