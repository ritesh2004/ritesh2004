
from turtle import *
import datetime
window = Screen()
window.bgcolor("black")
#creating the diagram
diagram = Turtle()
diagram.hideturtle()
diagram.speed(0)
diagram.penup()
diagram.goto(0,-275)
diagram.pendown()
diagram.pencolor("green")
diagram.pensize(25)
diagram.circle(300)
#numbers
pen = Turtle()
#number1
pen.penup()
pen.goto(125,216.5)
pen.pendown()
pen.hideturtle()
pen.pencolor("green")
pen.write("1",align="center",font=("Arial",30,"bold"))
#number2
pen.penup()
pen.goto(216.5,125)
pen.pendown()
pen.pencolor("green")
pen.write("2",align="center",font=("Arial",30,"bold"))
#number3
pen.penup()
pen.goto(250,0)
pen.pendown()
pen.pencolor("green")
pen.write("3",align="center",font=("Arial",30,"bold"))
#number4
pen.penup()
pen.goto(216.5,-125)
pen.pendown()
pen.pencolor("green")
pen.write("4",align="center",font=("Arial",30,"bold"))
#number5
pen.penup()
pen.goto(125,-216.5)
pen.pendown()
pen.pencolor("green")
pen.write("5",align="center",font=("Arial",30,"bold"))
#number6
pen.penup()
pen.goto(0,-250)
pen.pendown()
pen.pencolor("green")
pen.write("6",align="center",font=("Arial",30,"bold"))
#number7
pen.penup()
pen.goto(-125,-216.5)
pen.pendown()
pen.pencolor("green")
pen.write("7",align="center",font=("Arial",30,"bold"))
#number8
pen.penup()
pen.goto(-216.5,-125)
pen.pendown()
pen.pencolor("green")
pen.write("8",align="center",font=("Arial",30,"bold"))
#number9
pen.penup()
pen.goto(-250,0)
pen.pendown()
pen.pencolor("green")
pen.write("9",align="center",font=("Arial",30,"bold"))
#number10
pen.penup()
pen.goto(-216.5,125)
pen.pendown()
pen.pencolor("green")
pen.write("10",align="center",font=("Arial",30,"bold"))
#number11
pen.penup()
pen.goto(-125,216.5)
pen.pendown()
pen.pencolor("green")
pen.write("11",align="center",font=("Arial",30,"bold"))
#number12
pen.penup()
pen.goto(0,250)
pen.pendown()
pen.pencolor("green")
pen.write("12",align="center",font=("Arial",30,"bold"))
#creating center dot
dot = Turtle()
dot.penup()
dot.goto(0,20)
dot.pendown()
dot.color("white")
dot.shape("circle")
dot.shapesize(stretch_wid=1,stretch_len=1)
#creating hour hand
hHand = Turtle()
hHand.penup()
hHand.goto(0,20)
hHand.pendown()
hHand.shape("arrow")
hHand.color("white")
hHand.shapesize(stretch_len=15,stretch_wid=0.5)
#creating minutie hand
mHand = Turtle()
mHand.penup()
mHand.goto(0,20)
mHand.pendown()
mHand.shape("arrow")
mHand.color("white")
mHand.shapesize(stretch_len=23,stretch_wid=0.5)
#creating second hand
sHand = Turtle()
sHand.penup()
sHand.goto(0,20)
sHand.pendown()
sHand.shape("arrow")
sHand.color("dark red")
sHand.shapesize(stretch_len=22,stretch_wid=0.5)
#Defining function to movie hour hand
def movehHand():
   currentHourInternal = datetime.datetime.now().hour
   degree = (currentHourInternal - 15) * -30
   currentMinuteInternal = datetime.datetime.now().minute
   degree = degree + -0.5 * currentMinuteInternal
   hHand.setheading(degree)
   window.ontimer(movehHand, 60000)


#Defining function to minute hand
def movemHand():
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree = degree + (-currentSecondInternal * 0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand, 1000)

#Defining function to second hand
def movesHand():
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

window.ontimer(movehHand, 1)
window.ontimer(movemHand, 1)
window.ontimer(movesHand, 1)
window.exitonclick()
