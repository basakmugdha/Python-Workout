#Excercise 1 beyond 2: Number Guessing Game with base
import random

def guessing_game():
    '''Not only should you choose a random number, 
    but you should also choose arandom  number  base,  
    from  2  to  16,  in  which  the  user  should  submit  
    theirinput. If the user inputs “10” as their guess,
    you’ll need to interpret it in the correct  number  base;
    “10”  might  mean  10  (decimal),  or  2  (binary),  or  16(hexadecimal).
'''
    number = random.randint(1,100)
    rbase = random.choice((2,8,10,16))

    num = int(input("Guess the number (between 1 and 100) : "), base=rbase)

    
    while True :   
        if num>number:
            print("Too High")
        elif num == number:
            print("Just Right")
            break
        else:
            print("Too Low")
            
        num = int(input("Guess again : "), base=rbase)

if __name__ == '__main__':

    guessing_game()