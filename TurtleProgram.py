import turtle as t
import random
from turtle import Screen
t.colormode(255)


tim = t.Turtle()

def generate_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

directions = [0,90,180,270]
tim.pensize(25)
tim.speed("fastest")

for _ in range(200):
    tim.color(generate_random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()