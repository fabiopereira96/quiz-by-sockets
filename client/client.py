import socket
import os
import subprocess

s = socket.socket()
host = '192.168.1.2'
port = 9999

try:
    s.connect((host, port))
    print("Conexão estabelecida com o servidor.")

    while True:
        data = s.recv(1024)
        
        #info
        if data[:5].decode("utf-8") == '#info':
            print(data[5:].decode("utf-8"))
            s.send(str.encode("ok"))
        
        #question

except socket.error as msg:
    print("Não foi possível estabelecer uma conexão com o servidor na porta: " + 
    str(port) + " Error: " + str(msg))