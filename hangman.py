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

#print(programming_language)
print("WELCOME TO HANGMAN.PY")
time.sleep(2)
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
            elif x in [secretword[first_randword], secretword[second_randword]]:
                print('word already shown as HINT')
            elif x in alreadyguessed:
                time.sleep(1)
                print(' You have already guessed this letter')
            elif x not in 'abcdefghijklmnopqrstuvwxyz+':
                time.sleep(1)
                print(' please enter a letter.')
            else:
                return x

while True:


    alreadyguessed = ' '
    missedletters = ' '
    index_value1 = []
    index_value2 = []

    print()
    secretword = random_language_selection()
    print(' Guess this Word')

    first_randword = random.randint(0,len(secretword)-1)
    second_randword = random.randint(0,len(secretword)-1)
    secretword[first_randword]
    secretword[second_randword]
    

    while first_randword == second_randword:
        second_randword = random.randint(0,len(secretword)-1)

    index_value1 = [first_randword, second_randword]
    index_value2 = [first_randword, second_randword]
    print('Word Hints',secretword[first_randword], secretword[second_randword])

    for i in range(0,len(secretword)):
        print(' ', end=' ')
        if i in index_value1:
            print(secretword[i], end=' ')
        else:
            print('_', end=' ')
    
#    first_letter_of_secretword = secretword[0]
#    blank_board = ' ' + first_letter_of_secretword + '  _ '*(len(secretword)-1)
#    print(blank_board)   

    

    while True:
        
        #break the loop if player guess all words correctly. 
        if len(index_value2) == len(secretword):
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

        guess = user_input()


        #check if player guess is correct, and prints the board as well as user guess.
        if guess in secretword:

            alreadyguessed = alreadyguessed + guess
            for i in range(0,len(secretword)):
                if secretword[i] == guess:
                    index_value2.append(i)
                        
            #print('index value of user input in secretword:',index_value)

            
            for i in range(0,len(secretword)):
                print(' ', end=' ')
                if i in index_value2:
                    print(secretword[i], end=' ')
                else:
                    print('_', end=' ')
    

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
                if missedletters == ' ':
                    print('Missedguesses: 0')
                
                print(' Missedguesses:', missedletters)
                break



#if playagain is "no" then loop will break.
    
    if not play_again():
        break

        




















                



