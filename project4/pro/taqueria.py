def main():
    add_key()
food_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def add_key():
    x = 0
    while True:
        try:
            item = input("Item: ")
            i = item.title()
        except (EOFError, KeyboardInterrupt):
            break   
        try:
            if i in food_items:  
                y = food_items[i]
                x = x + y
                print("Total:" , f"${x:.2f}")
            else:
                pass
        except KeyError:
            pass
        else:
            pass
        

           
            


main()