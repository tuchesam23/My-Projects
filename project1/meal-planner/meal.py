def main():
    convert()

timeprompt = input("What time is it? ")

hours, minutes = timeprompt.split(":")  



def convert():
    if "7:00" <= timeprompt <= "8:00":
        print ("breakfast time")    

    elif "12:00" <= timeprompt <= "13:00":
       print ("lunch time") 

    elif "18:00" <= timeprompt <= "19:00":
       print ("dinner time")
    
    else:           
        print ()

main()

