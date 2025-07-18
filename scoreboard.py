from turtle import Turtle

#Constants fixed here...
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

#Create score_board class inherited from turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        #self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        #self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=('Arial', 16, 'normal'))