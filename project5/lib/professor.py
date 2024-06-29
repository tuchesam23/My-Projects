import random


def main():
    #call the get_level function
    level = get_level()
    #call the simulate_game function
    score = simulate_game(level)

    #print the correct score
    print ("Score: ", score)


#get the level whether it will be 1 or 2 or 3 digit number
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

#use the random module to generate random maddition problems depending on the level
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

#repeat for 3 times if the answer is wrong and give the right answer after 3 tries
def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

#add up the number of corect answers
def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()