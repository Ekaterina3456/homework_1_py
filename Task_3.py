# Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя». Сделайте ограничение
# на ввод отрицательных чисел и чисел больше 100 тысяч.

num = 0

while num < 1 or num > 100:
    num = int(input("введите числро от 1 до 100 "))

flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False

if num == 3:
    print("данное число простое")
elif flag:
    print("данное число простое")
else:
    print("данное число составное")



