import turtle
from turtle import *
import tkinter as tk
from tkinter import *


# functions turtle movement
def forward():
    Turtle.forward(50)
def forward_10(): 
    Turtle.forward(10)
def turn_right_90():
    Turtle.right(90)
def turn_right_10():
    Turtle.right(10)
def turn_left_90():
    Turtle.left(90)
def turn_left_10():
    Turtle.left(10)

# functions pen changes
def pen_size_up():
    pen_size = Turtle.pensize()
    pen_size = pen_size + 5
    Turtle.pensize(pen_size)
def pen_size_down():
    pen_size = Turtle.pensize()
    pen_size = pen_size - 5
    Turtle.pensize(pen_size)
def pen_up():
    Turtle.penup()
def pen_down():
    Turtle.pendown()

# functions Turtle visible or invisible
def hide_turtle():
    Turtle.hideturtle()
def show_turtle():
    Turtle.showturtle()

# functions utility
def home():
    Turtle.home()
def turtle_clear():
    Turtle.clear()
def turtle_reset():
    Turtle.reset()

def repeating_circle():
    rad = 10
    col = (Turtle.pencolor)
    s = 1
    for i in range (100):
        # veranderen van kleur bij 0, 25, 50, 75
        if i < 25:
            Turtle.pencolor("purple")
        elif i >= 25 and i < 50:
            Turtle.pencolor("green")
        elif i >= 50 and i < 75:
            Turtle.pencolor("blue")
        else:
            Turtle.pencolor("red")
        # cirkels maken
        col()
        Turtle.circle(rad)
        Turtle.right(90)
        rad = rad + 10
        s = s + 10000
        Turtle.speed(s)



if __name__ == "__main__":

    root = tk.Tk()

    canvas = tk.Canvas(root)
    canvas.config(width=1200, height=700)
    canvas.pack(side=tk.LEFT)

    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("lightgray")
    
    # turtle movement
    Label = tk.Label(root, text="Turtle movement", width=15, height=3)
    Label.pack()
    button = tk.Button(root, text="forward 50", command=forward, width=15)
    button.pack()
    button = tk.Button(root, text="forward 10", command=forward_10, width=15)
    button.pack()
    button = tk.Button(root, text="turn right 90", command=turn_right_90, width=15)
    button.pack()
    button = tk.Button(root, text="turn right 10", command=turn_right_10, width=15)
    button.pack()
    button = tk.Button(root, text="turn left 90", command=turn_left_90, width=15)
    button.pack()
    button = tk.Button(root, text="turn left 10", command=turn_left_10, width=15)
    button.pack()

    # turtle pen change
    Label = tk.Label(root, text="pen size changes", width=15, height=3)
    Label.pack()
    button = tk.Button(root, text="pen size up 5", command=pen_size_up, width=15)
    button.pack()
    button = tk.Button(root, text="pen size down 5", command=pen_size_down, width=15)
    button.pack()
    button = tk.Button(root, text="pen up", command=pen_up, width=15)
    button.pack()
    button = tk.Button(root, text="pen down", command=pen_down, width=15)
    button.pack()

    # turtle visible or invisible
    Label = tk.Label(root, text="Turtle visibility", width=15, height=3)
    Label.pack()
    button = tk.Button(root, text="hide turtle", command=hide_turtle, width=15)
    button.pack()
    button = tk.Button(root, text="show turtle", command=show_turtle, width=15)
    button.pack()

    # turtle utility
    Label = tk.Label(root, text="Turtle utility", width=15, height=3)
    Label.pack()
    button = tk.Button(root, text="home", command=home, width=15)
    button.pack()
    button = tk.Button(root, text="clear", command=turtle_clear, width=15)
    button.pack()
    button = tk.Button(root, text="reset", command=turtle_reset, width=15)
    button.pack()

    Label = tk.Label(root, text="Shapes", width=15, height=3)
    Label.pack()
    button = tk.Button(root, text="repeating circle", command=repeating_circle, width=15)
    button.pack()

    Turtle = turtle.RawTurtle(screen, shape="turtle")

    root.mainloop()
