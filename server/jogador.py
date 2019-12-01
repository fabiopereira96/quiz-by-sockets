
class Jogador():
    
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        self.score = 0.0
        self.winner = False

    def add_score(self, score):
        self.score += score
    
    def get_score(self):
        return self.score
    
    def get_connection(self):
        return self.connection
    
    def get_address(self):
        return self.address
    
    def set_winner(self):
        self.winner = True

    def get_winner(self):
        return self.winner
    
    def get_final_message(self):
        message = "\n Sua pontuação final foi de " + str(self.score)
        if self.winner:
            return "Parabéns, você venceu o Quiz." + message
        else:
            return "Não foi dessa vez... você perdeu o Quiz." + message