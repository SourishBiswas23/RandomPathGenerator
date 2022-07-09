import turtle

from pyparsing import col
import colors
import random

timmy = turtle.Turtle()
timmy.hideturtle()
my_screen = turtle.Screen()
timmy.pensize(3)
timmy.speed(0)
for i in range(1000):
    color = random.choice(colors.colors)
    timmy.pencolor(color)
    timmy.right(random.choice([0, 1, 2, 3, 4, 5])*60)
    xcoordinate = timmy.xcor()
    ycoordinate = timmy.ycor()
    if xcoordinate >= 960 or xcoordinate <= -960:
        timmy.penup()
        timmy.home()
        timmy.pendown()
    if ycoordinate >= 540 or ycoordinate <= -540:
        timmy.penup()
        timmy.home()
        timmy.pendown()
    timmy.forward(50)

my_screen.exitonclick()
