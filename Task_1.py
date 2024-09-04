# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

SPACE = " "
VERTICAL_STROKE = "|"
HYPHEN = "-"

width = int(input("введите длину прямоугольника "))
length = int(input("введите ширину прямоугольника "))

print(VERTICAL_STROKE + HYPHEN * (width - 2) + VERTICAL_STROKE)
for i in range(length - 2):
    print(VERTICAL_STROKE + SPACE * (width - 2) + VERTICAL_STROKE)
print(VERTICAL_STROKE + HYPHEN * (width - 2) + VERTICAL_STROKE)

