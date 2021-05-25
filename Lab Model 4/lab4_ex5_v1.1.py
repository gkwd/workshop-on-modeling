import math

def triangle_area():
    S = None
    area_type = int(input('Найди площадь по высоте(0) или по формуле Герона (1)?'))
    if area_type == 0: 
        a = float(input('A = '))
        h = float(input('h = '))
        S = 1/2 * a * h
    elif area_type == 1:
        a = float(input('A = '))
        b = float(input('B = '))
        c = float(input('C = '))
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    else: 
        print('Ввден неправильный аргумент')
    return S

def  square_area():
    square_side = float(input('A = '))
    return square_side * square_side

def  trapeze_area():
    a = float(input('Первое основанеи = '))
    b = float(input('Второе основание = '))
    h = float(input('Высота (h) = '))
    return ((a + b) / 2) * h

def circle_area(): 
    circle_type = int(input('Известен радиус да(1), нет(0)?'))
    S = None
    if circle_type == 1:
        r = float(input('Радиус равен: '))
        S = math.pi * r**2
    elif circle_type == 0:
        d = float(input('Диаметр равен: '))
        S = 1/4 * math.pi * d**2
    else: 
        print('Ввден неправильный аргумент')
    return S



figure_type = input("Круг (C), Квадрат(S), Треугольник (T), Траперция(TP): ")
if figure_type == 'C':
    print("Площадь круга: ", circle_area())

elif figure_type == 'S':
    print("Площадь квадрата ", square_area())

elif figure_type == 'T':
    print("Площадь треугольника: ", triangle_area())

elif figure_type == 'TP':
    print("Площадь траперции: ", trapeze_area())
else: 
    print('Мы не может расчитать площадь этой фигуры, на данный момент')