#Excercise 1 beyond 3: Word Guessing Game
from random_word import RandomWords

def guessing_game():
    '''returns a random integer between 1 and 100'''
    r = RandomWords()
    return r.get_random_word()
    
    

if __name__ == '__main__':

    print('Hmmmm.... let me pick a word')
    word = guessing_game()
    guess = input(f"Guess the word ({len(word)} characters) : ")

    # only 6 guesses so the game is less tedious
    #the for loop can be replaced with 'while True:' for the original trap style game
    for _ in range(5): 
        if guess>word:
            print("You're far ahead in the dictionary")
        elif guess == word:
            print("YOU GUESSED IT!")
            break
        else:
            print("You're far behind in the dictionary")

        word = input('Guess again :') 
    print(word+' is the word!')
    