import sys 
import random
from pyfiglet import Figlet

figlet = Figlet()

#check if the zero line argument is zero or two and assign it to a variable
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit(1)

#get user"s input
user_input = input("Input: ")

#get a list of available fonts with code like this
figlet.getFonts()

#set the font to either what is given on the CLI or a random font
if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("invalid font")
        sys.exit(1)
#when no font given, set to a random font
else:
    font = random.choice(figlet.getFonts())

#print the result
output_font = figlet.renderText(user_input)
print("Output: ")
print(output_font)
