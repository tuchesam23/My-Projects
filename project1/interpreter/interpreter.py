def main():
    calculator()

Expression = (input("Expression: "))


x, y, z = Expression.split(" ")

def calculator():
    if y == "+":
        add = float(x) + float(z)
        print(f"{add:.1f}")

    elif y == "-":
       subtract = (float(x) - float(z))
       print(f"{subtract:.1f}")

    elif y == "/":
        divide = (float(x) / float(z))    
        print(f"{divide:.1f}")

    elif y == "*":
        multiply = (float(x) * float(z))    
        print(f"{multiply:.1f}")    

main ()



