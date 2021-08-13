"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""

if __name__ == '__main__':
    for i in range(101):
        print(i)
    for i in range (101):
        print(100-i)
    for i in range (51):
        if i!= 0:
            print(i*2)
    for i in range(1,100,2):
        print(i)
    for i in range(501):
        if i%2==0:
            print(str(i) +" is an even number")
        else:
            print(str(i) +' is an odd number')
    for i in range(7,784,7):
        print(i)
    year= 2008
    for i in range(13):
        year=year+1
        print(' In ' + str(year) + ' I was ' + str(i) + ' years old ')

    for i in range(3):
        for f in range(3):
            print(str(i)+ ' ' + str(f))

    for i in range(3):
        str2 = ' '
        for k in range (1,4):
            str2 += str(k + (i*3)) + ' '
        print(str2)

    for i in range(10):
        str2= ' '
        for b in range(1,11):
            str2 += str(b + (i*10)) + ' '
        print(str2)

    for i in range (1,7):
        str2 = ' '
        for c in range(i):
           str2 += "* "
        print(str2)
    pass
