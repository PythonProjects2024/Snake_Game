from turtle import Screen
from Modules.snake import Snake
from Modules.food import Food
from Modules.scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Snake Game")
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.food_refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for segment in snake.portion[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
        





screen.exitonclick()
