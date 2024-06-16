import turtle as t 
import random
from turtle import Screen 
t.colormode(255)

tim =t.Turtle()
def generate_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in  range(int( 360 / size_of_gap )):
        tim.color(generate_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() +size_of_gap )

draw_spirograph(5)
screen = Screen()
screen.exitonclick()