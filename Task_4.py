# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

count = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
assumption = 0

while count != 0 or assumption != num:
    assumption = int(input("попробуйте угодать число "))
    if assumption < num:
        print("загаданное число больше ")
    else:
        print("загаданное число меньше")
    count -= 1
    if assumption == num:
        print("вы угадали число")

if count == 0:
    print("у вас закончились попытки ")
if 2<4:
    print(5)