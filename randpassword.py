from random import randint

def password():
    a = ''
    for i in range(randint(7,10)):
        a = chr(randint(33,126))+a
    return a

#print(password()) для упражнения 8