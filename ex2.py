print("Введите стороны прямоугольника")
a = int(input())
b = int(input())

k = 0


def Square(a, b):
    global k
    k += 1
    if a > b:
        print(f"Сторона квадрата {k}: {b}")
        return Square(a - b, b)
    elif a < b:
        print(f"Сторона квадрата {k}: {a}")
        return Square(a, b - a)
    else:
        print(f"Сторона квадрата {k}: {a}")
        print(f"Количество квадратов: {k}")
        return

Square(a,b)