def main():
    input_string = input("Input: ")

    print("Output: ", removevowel(input_string))

def removevowel(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    newstring = text
    text = text.lower()
    for char in text:
        if char in vowels:  
             newstring = newstring.replace(char, "")
    return newstring
main()
