"""
Print out the first 12 numbers of the fibonacci sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...
https://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  There is more than one way to code a solution to this.
    #  The following steps give you some guidelines for one of them.
    #  1. Declare and initialize three int variables: number1, number2,
    #     and sum.
    #  2. Initialize number1 and number2 to the first two numbers of the
    #     fibonacci sequence (0 and 1) and print both numbers.
    #  3. Use a for loop that calculates the sum of the two numbers and
    #     prints it. The for loop should repeat 10 times.
    #  4. Now try to figure out how to change the variables before the for
    #     loop repeats so the sequence of numbers is correct.
    num1 = 0
    num2 = 1
    sum = 1
    print('0')
    print('1')
    for i in range (100):
        sum = num1 + num2
        print(sum)
        num1 = num2
        num2 = sum
    pass
