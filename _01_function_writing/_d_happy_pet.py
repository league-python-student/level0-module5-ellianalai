"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
def feed(score,name):
    if name == 'dog':
        return score+4
    elif name == 'turtle':
        return score+3
    elif name == 'hamster':
        return score+ 2
    else:
        return score
def walk(score,name):
    if name == 'dog':
        return score + 2
    elif name == 'turtle':
        return score -5
    elif name == 'hamster':
        return score + 1
    else:
        return score
def play(score, name):
    if name == 'dog':
        return score + 6
    elif name == 'turtle':
        return score + 1
    elif name == 'hamster':
        return score + 5
    else:
        return score
def do_business(score, name):
    if name == 'dog':
        return score - 3
    elif name == 'turtle':
        return score - 6
    elif name == 'hamster':
        return score - 5
    else:
        return score
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    happiness = 0
    pet = simpledialog.askstring(title='', prompt='what type of pet do you want? A dog, a turtle, or a hamster?')
    while happiness<20:
        activities= simpledialog.askstring(title ='', prompt = 'Do you want to feed, walk, play with your pet? Or do you want your pet to do their business?')

        if activities =='feed':
            score = feed(happiness,pet)
            messagebox.showinfo(title='', message='Your %s has %s points, it gained %s points'%(pet, score,score-happiness))
            happiness = score
        elif activities == 'walk':
            score = walk(happiness,pet)
            messagebox.showinfo(title='', message='Your %s has %s points, it gained %s points' % (pet, score, score-happiness))
            happiness = score
        elif activities == 'play':
            score = play(happiness,pet)
            messagebox.showinfo(title='', message='Your %s has %s points, it gained %s points' % (pet, score, score-happiness))
            happiness = score
        elif activities == 'Do your business':
            score = do_business(happiness,pet)
            messagebox.showinfo(title='', message='Your %s has %s points, it gained %s points' % (pet, score, score-happiness))
            happiness = score
        else:
            messagebox.showerror(title='', message='please insert an activity, feed, walk, play, and do your business')
    messagebox.showinfo(title='',message= 'You have now achieved full happiness and your pet dies at full happiness too!')
    pass
