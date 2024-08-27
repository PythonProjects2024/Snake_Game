from hmac import new

from turtle import Turtle
import random
import turtle



class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.food_refresh()

    def food_refresh(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)
        
       

    
         




    

    