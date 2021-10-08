from human import Human 
from ai import AI
class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        self.round_count = 1
        
