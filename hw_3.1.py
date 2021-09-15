def my_funcion (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y isn't be a zero"
    except ValueError:
        return "enter only number"
print(my_funcion(int(input("Enter x = ")), int(input("Enter y = "))))
