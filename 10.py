import randpassword
import checkpassword

a = 0
b = str(randpassword.password())


while checkpassword.ChekPassword(b) != True:
    a +=1
    b = str(randpassword.password())


print('Пароль: ', b)
print('Колличество попыток создания пароля: ', a)