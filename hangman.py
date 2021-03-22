# HANGMAN
import random
import time
programming_language = '''java python ruby javascript c++ php mysql html go algorithm datastructure programming keyboard mouse processor graphicscard motherboard network list dictionary tuple set google apple facebook microsoft netflix amazon yahoo adobe coursera udemy edx samsung cisco'''.split()


HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    o   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    o   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    o   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    o   |
   /|\  |
        |
        |
  =========''', '''


    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
  =========''']


print("WELCOME TO HANGMAN.PY")
print(' You have to guess the correct word. it can be a very common input device name like "mouse".\n or a famous programming language\n or, common programming term like "programming" itself\n or, any kind of datastructure or, a name from FAANG\n or, a well known E-Learning platform.\n but, if you guess any incorrect word I will start hanging "HANGMAN" in step by step manner.')
time.sleep(9)
print()
print('Let us start')
print()
print('################################################')
print()
print()


#Returns a random string(programming_language) from the lists.
def random_language_selection():
    random_index_value = random.randint(0,len(programming_language))
    random_language = programming_language[random_index_value]
    return random_language



#asks the player to play again, and later will use to break the while loop.
def play_again():
    return input(' phir se khelna hai kya? (yes/no): ').lower().startswith('y')
     
    
def user_input():
        print()
        while True:
            time.sleep(1)
            x = input('\n enter your guess: ').lower()
            if len(x) != 1:
                time.sleep(1)
                print(' You can only guess one letter at a time.')
            elif x in alreadyguessed:
                time.sleep(1)
                print(' You have already guessed this letter')
            elif x not in 'abcdefghijklmnopqrstuvwxyz':
                time.sleep(1)
                print(' please enter a letter.')
            else:
                return x

while True:
    
    print()
    secretword = random_language_selection()
    print(' Guess this Word')
    first_letter_of_secretword = secretword[0]
    blank_board = ' ' + first_letter_of_secretword + '  _ '*(len(secretword)-1)
    print(blank_board)   

    
    alreadyguessed = ' '
    missedletters = ' '
    index_value = []

    while True:
        
        #break the loop if player guess all words correctly. 
        if len(index_value) == len(secretword):
            time.sleep(1)
            print('\n\n ')
            for i in [' checking your answer', '.', '.', '.']:
                time.sleep(1)
                print(i, end=' ')
            
            time.sleep(2)
            print()
            print('\n apne sahi name guess kiya..aap..jeet gye hai!!! ')
            print(' Correct letter was:', secretword)
            print(' Missedguesses:', missedletters)
            time.sleep(2)
            break


        #takes user input
        guess = user_input()

        #check if player guess is correct, and prints the board as well as user guess.
        if guess in secretword:
            alreadyguessed = alreadyguessed + guess
            for i in range(0,len(secretword)):
                if secretword[i] == guess:
                    index_value.append(i)
                       

            
            for i in range(0,len(secretword)):
                print(' ', end=' ')
                if i in index_value:
                    print(secretword[i], end=' ')
                else:
                    print('_', end=' ')
    


#if player guess is incorrect, then else block will prints a particular hangman ASCII art
#form HANGMANPICS according to the length of string in missed words. and at the same time nested if block will checks if
#has reached to last ASCII art beacuse last ASCII art is considered as end of the game.

        else:
            alreadyguessed = alreadyguessed + guess
            time.sleep(1)
            print(' Wrong guess...')
            missedletters = missedletters + guess
            print(HANGMANPICS[len(missedletters)-1])
            

            if len(missedletters) == len(HANGMANPICS):
                
                print(' haar gye! because hangman is hanged')
                print()
                time.sleep(1)
                print(' Correct letter was:', secretword)
                time.sleep(1)
                print(' Missedguesses:', missedletters)
                break



#if playagain is "no" then loop will break.
    
    if not play_again():
        break

        




















                



