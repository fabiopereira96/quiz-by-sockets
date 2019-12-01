import socket
import os
import time
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
        elif data[:9].decode("utf-8") == '#question':
            print("Responda a questão abaixo:")
            print(data[9:].decode("utf-8"))
            print("\nInforme a alternativa (A, B, C ou D):")
            answer = input()
            s.send(str.encode(answer))
        elif data[:7].decode("utf-8") == '#answer':
            print(data[7:].decode("utf-8"))
            time.sleep(1)
            s.send(str.encode("ok"))
        else:
            print(data.decode("utf-8"))
            time.sleep(1)
            s.send(str.encode("ok"))

except socket.error as msg:
    print("Não foi possível estabelecer uma conexão com o servidor na porta: " + 
    str(port) + " Error: " + str(msg))