from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = 'AI'
        super().__init__()
        pass

    def gesture_select(self, gesture_list):
        self.choice = random.choice(gesture_list)
