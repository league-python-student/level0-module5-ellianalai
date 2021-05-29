"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def square(turtle1):
     for i in range (4):
         turtle1.forward(50)
         turtle1.right(90)
def triangle(turtle1):
    for i in range (3):
        turtle1.forward(50)
        turtle1.left(120)
def circle(turtle1):
    turtle1.circle(50,360,100)


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #   1. Create a turtle.
    ellie = turtle.Turtle()
    shapes= simpledialog.askstring(title='Shapes', prompt='What shape do you want to draw? A square, triangle, circle, or house?')

    if shapes == 'square':
        square(ellie)
    if shapes == 'triangle':
        triangle(ellie)
    if shapes == 'circle':
        circle(ellie)
    if shapes == 'house':
        square(ellie)
        triangle(ellie)
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)

    turtle.done()
    pass
