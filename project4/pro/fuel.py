def main():
    fuel_checker("Fraction: ")

def fuel_checker(prompt):
    while True:
        try:
            fraction = (input(prompt))

            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            
            if x <= y:
                z = (x / y) * 100
                
                if z == 100:
                    print("F")
                    break
                elif z == 0 :
                    print("E")
                    break
                else:
                    print(f"{z:.0f}%")
                    break    
        except(ValueError, ZeroDivisionError):
            pass
        pass
main()