def factorial(n):
    if z == 0:
        return 1
    else:
        return z * factorial(z-1)

number = int(input("введи число: "))
out = factorial(number)
print(f"факториал числа {number} равен {out}")
