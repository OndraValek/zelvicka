from turtle import *
import math
import random

def spirala():
    shape("turtle")
    color("white")
    bgcolor("black")
    for i in range(100):
        forward(i)
        left(20)

def hvezda():
    bgcolor("black")
    color("white")
    speed(200)
    for i in range(5):
        forward(100)
        right(144)

def strom():
    def drawRectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()

        # Function to draw triangle

    def drawTriangle(t, length, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(length)
        t.left(135)
        t.forward(length / math.sqrt(2))
        t.left(90)
        t.forward(length / math.sqrt(2))
        t.left(135)
        t.end_fill()

        # Set the background color

    screen = Screen()
    screen.bgcolor("black")

    # Creating turtle object
    tip = Turtle()
    tip.color("black")
    tip.shape("turtle")
    tip.speed(2)

    # Tree base
    tip.penup()
    tip.goto(100, -130)
    tip.pendown()
    drawRectangle(tip, 20, 40, "brown")

    # Tree top
    tip.penup()
    tip.goto(65, -90)
    tip.pendown()
    drawTriangle(tip, 90, "lightgreen")
    tip.penup()
    tip.goto(70, -45)
    tip.pendown()
    drawTriangle(tip, 80, "lightgreen")
    tip.penup()
    tip.goto(75, -5)
    tip.pendown()
    drawTriangle(tip, 70, "lightgreen")

def prekvapeni():
    speed(10)
    while True:
        forward(180)
        left(70)
        forward(60)
        right(random.randint(40, 70))

        penup()
        setposition(0, 0)
        pendown()

        right(random.randint(2, 10))

