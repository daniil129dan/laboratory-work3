def FromInttoStr(a):
    if (12>=a>=0):
        if a == 0:
            return 'first'
        elif a == 1:
            return 'second'
        elif a == 2:
            return 'third'
        elif a == 3:
            return 'fourth'
        elif a == 4:
            return 'fifth'
        elif a == 5:
            return 'sixth'
        elif a == 6:
            return 'seventh'
        elif a == 7:
            return 'eighth'
        elif a == 8:
            return 'ninth'
        elif a == 9:
            return 'tenth'
        elif a == 10:
            return 'eleventh'
        elif a == 11:
            return 'twelfth'
        else:
            return


for i in range(12):
    print(i+1,': ', FromInttoStr(i))