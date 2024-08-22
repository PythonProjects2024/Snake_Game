from math import gamma
from tkinter import SEL
from turtle import Turtle, down, forward

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.portion = []
        self.make_snake()
        self.head = self.portion[0]

    def make_snake(self):

        for position in STARTING_POSITION:
            new_snake = Turtle("square")
            new_snake.shapesize(0.1,1)
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.portion.append(new_snake)

                   

    def move(self):
        for por_num in range(len(self.portion)-1, 0, -1):
            new_x = self.portion[por_num - 1].xcor()
            new_y = self.portion[por_num - 1].ycor()
            self.portion[por_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

     
    def set_direction(self, heading):
        if self.head.heading() != heading:
            self.head.setheading(heading)
            for segmant in self.portion:
                segmant.setheading(heading)


    def up(self):
        if self.head.heading() != DOWN:
            self.set_direction(UP)

    def down(self):
        if self.head.heading() != UP:
            self.set_direction(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.set_direction(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.set_direction(LEFT)
        

    






