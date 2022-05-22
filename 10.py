import randpassword
import checkpassword

a = 0
b = str(randpassword.Password())


while checkpassword.ChekPassword(b) != True:
    a +=1
    b = str(randpassword.Password())


print('Пароль: ', b)
print('Колличество попыток создания пароля: ', a)
