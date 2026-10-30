# Terrence Barnes Jr.
# 10/30/2026
# P4LAB1
# This program uses a while loop and a for loop to draw a triangle and square to create a house.

import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle House")

t = turtle.Turtle()
t.color("darkred")
t.pensize(4)
t.speed(3)

t.penup()
t.goto(-100, -100)
t.pendown()

count = 0
while count < 4:
    t.forward(200)
    t.left(90)
    count += 1

t.penup()
t.goto(-100, 100)
t.pendown()

for side in range(3):
    t.forward(200)
    t.left(120)

t.hideturtle()

turtle.done()
