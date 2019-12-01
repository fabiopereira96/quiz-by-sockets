import sys
import threading
import time
from queue import Queue
import quiz_socket as qsocket
import quiz as qquestions
import jogador as jg

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
connections = []
address = []

def create_workers(quizServer, quiz):
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work, args=(quizServer, quiz,))
        t.daemon = True
        t.start()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

def work(quizServer, quiz):
    while True:
        x = queue.get()
        if x == 1:
            quizServer.bind()
            quizServer.init_connections()
        if x == 2:
            start_game(quizServer, quiz)
        queue.task_done()

def start_game(quizServer, quiz):
    is_started = False
    while True:
        jogadores = []
        connections = quizServer.get_connections()
        address = quizServer.get_address()
        if len(connections) > 1 and not is_started:
            is_started = True
            print("Adicionando jogadores...")
            for conn in connections:
                jogadores.append(jg.Jogador(conn, address))
                print("Adicionando " + str(conn) + str(address))
            print("Jogadores adicionados...")
            print("Iniciando partida...")

            while not quiz.is_end_game():
                question = quiz.get_current_question()
                answer = quiz.get_answer_by_current_question()

                for jogador in jogadores:
                    jog_awnswer = quizServer.send_jogador_question(jogador, str(question))
                    print("Retorno do jogador: "+str(jog_awnswer))
                    jogador.add_score(quiz.get_score_by_answer(jog_awnswer))
            
            index = -1
            score = -1
            for i, jogador in enumerate(jogadores):
                if jogador.get_score() > score:
                    score = jogador.get_score()    
                    index = i
            if score > -1:
                jogadores[index].set_winner()
                
            #Encerra o jogo com as mensagens por jogador
            for jogador in jogadores:
                quizServer.send_final_message(jogador.get_connection(), jogador.get_final_message())
        else:
            print("Aguardando jogadores...")
            time.sleep(2)

if __name__ == "__main__":
    quizServer = qsocket.SocketQuiz()
    quiz = qquestions.Quiz()
    create_workers(quizServer, quiz)
    create_jobs()
