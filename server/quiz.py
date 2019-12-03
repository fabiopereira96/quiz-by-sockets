class Quiz():

    def __init__(self):
        self.current_question = -1
        self.questions = [
                ['Dentre os itens abaixo, qual não corresponde a uma diferença entre UDP e TCP?\n',
                    ['A) Orientação a conexão\n',
                        'B) Garantia de entrega\n',
                        'C) Garantia de ordenação de pacotes\n',
                        'D) Usa segmentação de pacotes'],
                    100,
                    'D'],
                ['Dentre os itens abaixo, qual é o principal motivo para a migração de IPv4 para IPv6?\n',
                    ['A) Performance da comunicação\n',
                        'B) IPv6 tem garantia de entrega de pacotes\n',
                        'C) Proximidade do limite de endereços possíveis com o IPv4\n',
                        'D) IPv6 tem uma verificação de erros de pacotes não disponível no IPv4'],
                    150,
                    'C'],
                ['Qual a função do CheckSum no cabeçalho dos protocolos TCP/UDP?\n',
                    ['A) Tamanho do pacote\n',
                        'B) Verificar integridade do Pacote\n',
                        'C) Confirmar o recebimento do Pacote\n',
                        'D) Informar o destino do PAcote'],
                    50,
                    'B'],
                ['Para estabelecimento da conexão entre cliente e servidor, ocorre o Handshake de quantas vias?\n',
                    ['A) Uma via\n',
                        'B) Duas vias\n',
                        'C) Três vias\n',
                        'D) Quatro vias'],
                    50,
                    'C'],
                ['Seguindo o modeo padrão de subrede a.b.c.d/x, o que a máscara 192.168.0.0/23 quer dizer?\n',
                    ['A) Existem 512 IPs disponíveis nessa rede para uso e todos começam com 192.168.0 ou 192.168.1\n',
                        'B) Existem 23 IPs disponiveis nessa rede e todos começam com 192.168.0\n',
                        'C) Existem 256 IPs disponiveis e todos começam com 192.168.23\n',
                        'D) Existem 23 roteadores nessa subrede e todos começam com 192.168.0.0'],
                    200,
                    'A']]
    
    def get_questions(self):
        return self.questions
    
    def get_current_question(self):
        self.current_question = self.current_question + 1
        return self.questions[self.current_question][:2]
    
    def get_answer_by_current_question(self):
        return self.questions[self.current_question][3]
    
    def get_score_by_answer(self, answer):
        if self.get_answer_by_current_question() == answer:
            return self.questions[self.current_question][2]
        else:
            return 0
    
    def is_end_game(self):
        return self.current_question == len(self.questions)-1

#-----------------------------------------------------#
#                   Example:

# quiz = Quiz()
# score = 0
# print(quiz.get_current_question())
# print("\nInforme a alternativa (A, B, C ou D):")
# answer = input()
# if answer == quiz.get_answer_by_current_question():
#     print("Você acertou a questão.")
#     score += quiz.get_score_by_current_question()
# else:
#     print("Você errou a questão.")
# print("Sua pontuacao atual é: " + str(score))

# print(quiz.get_current_question())
# print("\nInforme a alternativa (A, B, C ou D):")
# answer = input()
# if answer == quiz.get_answer_by_current_question():
#     print("Você acertou a questão.")
#     score += quiz.get_score_by_current_question()
# else:
#     print("Você errou a questão.")
# print("Sua pontuacao atual é: " + str(score))
