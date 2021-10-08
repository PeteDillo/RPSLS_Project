class Player:
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
        self.choice = self.gesture_list[int(input())]
        self.choice.validation()
        print(f"{self.name} selects {self.choice}!")

    
