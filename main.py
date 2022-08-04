from turtle import Screen
from time import sleep
from food import Food
from scoreboard import Scoreboard
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake!')
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    
    # Detect collision with food
    # Use distance() from Turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()


screen.exitonclick()