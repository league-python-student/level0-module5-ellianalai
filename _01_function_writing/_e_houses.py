"""
Have the turtle draw a row of houses.
"""
import random
from tkinter import messagebox, simpledialog, Tk
import turtle
def pointy_roof(turtle1):
       turtle1.left(45)
       turtle1.forward(25)
       turtle1.right(90)
       turtle1.forward(25)
       turtle1.left(45)
def flat_roof(turtle1):
    turtle1.forward(50)
def draw_house(turtle1,height):

        turtle1.pencolor('green')
        turtle1.pensize(15)
        turtle1.forward(30)
        turtle1.pencolor('brown')
        turtle1.pensize(10)
        turtle1.left(90)
        turtle1.forward(height)
        turtle1.right(90)
        if height > 175:
            flat_roof(turtle1)
        else:
            pointy_roof(turtle1)
        turtle1.right(90)
        turtle1.forward(height)
        turtle1.pencolor('green')
        turtle1.pensize(15)
        turtle1.left(90)
        turtle1.forward(30)





if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    ellie = turtle.Turtle()
    ellie.penup()
    ellie.goto(-300,-200)
    ellie.pendown()
    for i in range(10):
        draw_house(ellie,random.randint(20,300))

    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    turtle.done()
    pass
