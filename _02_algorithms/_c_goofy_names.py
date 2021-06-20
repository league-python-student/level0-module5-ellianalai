"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    name = simpledialog.askstring(title='',prompt='Enter your name')
    goofy_name = ''
    for i in range(len(name)):
        if i%2==0:
            goofy_name+= name[i].upper()
        else:
            goofy_name += name[i].lower()
    messagebox.showinfo(None,goofy_name)
    pass
