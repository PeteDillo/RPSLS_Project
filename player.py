from random import choice


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = ""
        self.gesture_list = ["rock","paper","scissors","lizard","spock"]


    def gesture_select(self):
        print("Choose your gesture:")
        index = 0
        for gesture in self.gesture_list:
            print(f"Press {index} for {gesture}")
            index += 1
        player_choice = int(input())
        self.validation(player_choice)
        if player_choice > 4 and player_choice < 0 :
            self.gesture_select()
        self.choice = self.gesture_list[player_choice]
        print(f"{self.name} selects {self.choice}!")


    def validation(self, choice):
            if choice != int:
                self.validation
            elif choice > 4:
                self.validation
            else:
                pass