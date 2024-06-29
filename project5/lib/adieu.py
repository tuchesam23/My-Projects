import inflect

p = inflect.engine()

#create list to keep track of names
names = []

#loop fforever
while True:

#get user input
    try:
        name = input("Name: ").title()
        names = names + [name]
#create new line and stop the loop        
    except KeyboardInterrupt:
        print()
        break
    
#print using the inflext module
output = p.join(names)
print("Adieu, adieu to " + output)
