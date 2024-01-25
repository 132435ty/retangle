def rectangle(length, width):
    p = length * width
    return p

length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

x = rectangle(length, width)
print("Площадь прямоугольника:", x)
