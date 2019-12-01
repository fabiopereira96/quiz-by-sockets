import socket
import sys
import time
from queue import Queue

class SocketQuiz():
    
    def __init__(self):
        try:
            self.connections = []
            self.address = []
            self.host = ""
            self.port = 9999
            self.socketConnection = socket.socket()
        except socket.error as msg:
            print("Não foi possível criar conexao inicial do socket: " + str(msg))

    def init_connections(self):
        #Fecha todas as conexoes ja existentes antes de iniciar loop
        self.close_connections()
        while True:
            try:
                #Aguarda nova conexao
                conn, addrs = self.socketConnection.accept()
                self.socketConnection.setblocking(1)

                #Adiciona novo cliente a lista de conexoes
                self.connections.append(conn)
                self.address.append(addrs)

                print("\nNova conexao estabelecida com: " + addrs[0])
                print("\nTemos um total de " + str(len(self.connections)) + " conexoes")
                self.send_waiting_message(conn)

            except socket.error as msg:
                print("Error ao aceitar novas conexoes" + str(msg)) 

    def close_connections(self):
        for conn in self.connections:
            conn.close()
        del self.connections[:]
        del self.address[:]

    def bind(self):
        try:
            print("\nIniciando socket na porta: " + str(self.port))
            self.socketConnection.bind((self.host, self.port))
            self.socketConnection.listen(5)
        except socket.error as msg:
            print("\nError ao iniciar socket " + str(msg) + "\n" + " Reconectando em 1seg...")
            time.sleep(1)
            self.bind()

    def show_connections(self):
        list_conn = ''
        for i, conn in enumerate(self.connections):
            try:
                conn.send(str.encode(' '))
                conn.recv(20480)
            except:
                del self.connections[i]
                del self.address[i]
                continue
            list_conn += str(i) + "   " + str(self.address[i][0]) + "   " + str(self.address[i][1]) + "\n"
        print("------------------------------------------------------" + "\n" 
            + "\t\t Conexoes existentes \t\t\n" + list_conn)

    def send_jogador_question(self, jogador, question):
        conn = jogador.get_connection()
        try:
            conn.send(str.encode("#question" + question))
            byte_expected = self.utf8len('A')
            answer = conn.recv(byte_expected)
            while answer == None:
                answer = conn.recv(byte_expected)
            return str(answer)[2]
        except socket.error as msg:
            print("Não foi possível enviar a mensagem para a conexão: " + str(conn) + str(msg))

    def send_waiting_message(self, conn):
        length_conn = len(self.connections)
        self.send_message(conn, "#info Aguardando um adversário para você. Em instantes o Quiz será iniciado!")
        if length_conn > 1:
            for i, conni in enumerate(self.connections):
                self.send_message(conni, "#info Boa notícia, seu adiversário já está conectado e iremos iniciar o Quiz!")
            
    def send_message(self, conn, message):
        try:
            length_recv = self.utf8len("ok")
            conn.send(str.encode(message))
            answer = conn.recv(length_recv)
            while answer == None:
                answer = conn.recv(length_recv)
        except:
            print("Não foi possível enviar a mensagem para a conexão: " + str(conn) + str(message))
    
    def send_final_message(self, conn, message):
        try:
            length_recv = self.utf8len("ok")
            conn.send(str.encode(message))
            conn.recv(length_recv)
        except:
            print("Não foi possível enviar a mensagem para a conexão: " + str(conn) + str(message))

    def get_connected_client_by_id(self, id):
        try:
            return self.connections[id]
        except:
            print("Cliente invalido")
            return None

    def get_connections(self):
        return self.connections
    
    def get_address(self):
        return self.address
    
    def utf8len(self, s):
        return len(s.encode('utf-8'))