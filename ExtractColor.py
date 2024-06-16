import colorgram
import turtle as t
import random
from turtle import Screen
# rgb_colors =[]
# colors=colorgram.extract('images/color-shapes.png',6)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b

#     rgb_colors.append((r,g,b))

# print(rgb_colors)
t.colormode(255)
tim= t.Turtle()

color_list =[(255, 254, 254), (28, 255, 254), (22, 22, 255), (255, 18, 255), (12, 254, 8), (254, 254, 6)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots =100
tim.speed("fastest")

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=Screen()
screen.exitonclick()