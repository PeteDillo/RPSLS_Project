from player import Player
import random

class AI(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        pass

    def gesture_select(self):
        self.choice = random.choice(self.gesture_list)
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

    