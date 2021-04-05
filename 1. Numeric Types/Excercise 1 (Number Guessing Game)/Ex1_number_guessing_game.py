#Excercise 1 : Number Guessing Game
import random

def guessing_game():
    '''returns a random integer between 1 and 100'''
    return random.randint(1,100)
    
    

if __name__ == '__main__':

    num = int(input("Guess the number (between 1 and 100) : "))
    number = guessing_game()

    # using the := expression assignment operator (walrus operator)
    while num := int(input("Guess again : ")):   
        if num>number:
            print("Too High")
        elif num == number:
            print("Just Right")
            break
        else:
            print("Too Low")

    