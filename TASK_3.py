# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
if x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print("II четверть")
elif x < 0 and y < 0:
    print("III четверть")
elif x > 0 and y < 0:
    print("IV четверть")
else:
    print("Введён ноль, отмена программы")

