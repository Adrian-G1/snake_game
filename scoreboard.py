from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.penup()
        self.sety(280)
        self.color("white")
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def read_high_score(self):
        with open("data.txt") as file:
            return int(file.read())
        
    def update_high_score(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))