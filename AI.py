from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = 'AI'
        super().__init__()
        pass

    def gesture_select(self, gesture_list):
        self.choice = random.choice(gesture_list)
        if(self.choice == "rock"):
            print(f"Player 2 selects {self.choice}.")
        elif(self.choice == "paper"):
            print(f"Player 2 selects {self.choice}.")    
        elif(self.choice == "scissors"):
            print(f"Player 2 selects {self.choice}.")        
        elif(self.choice == "lizard"):
            print(f"Player 2 selects {self.choice}.")  
        elif(self.choice == "spock"):
            print(f"Player 2 selects {self.choice}.")  


