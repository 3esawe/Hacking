import socket 

socket.setdefaulttimeout(4)

s = socket.socket()
s.connect(("216.58.208.68",443))
ans = s.recv(1024)
print ans
