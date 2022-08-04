from turtle import Turtle

STARTING_POSITIONS= [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    
    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            body = Turtle(shape='square')
            body.color('white')
            body.penup()
            body.goto(position)
            self.snake_body.append(body)

    
    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        
        self.head.fd(MOVE_DISTANCE)
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
