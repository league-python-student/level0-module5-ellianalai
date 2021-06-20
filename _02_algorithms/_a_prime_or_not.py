"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk,sys


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    number = simpledialog.askinteger(title='number', prompt= 'Type in a number')
    for i in range(2,number):
        if number%i==0:
            messagebox.showinfo(title='',message='Your number is not a prime number')
            sys.exit()
    messagebox.showinfo(title='',message='Your number IS a prime number')

    pass
