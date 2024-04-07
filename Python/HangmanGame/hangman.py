#Step 1 
import random
import hangman_words 
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
index=random.randint(0,len(hangman_words.word_list)-1)
word=hangman_words.word_list[index].lower()

blank=["_"]*len(word)
boolean=True
lives=6
ind=len(stages)-1

while boolean:
    user=input("Guess a letter....!!\n")
    if user in word:
        print("You have already guesses the letter...Please try different...!!!")
    letter_list=list(word)
    for i in range(len(letter_list)):
        if user==letter_list[i]:
            blank[i]=user
    if user not in word:
        print(stages[ind])
        ind-=1
        lives-=1
        if lives==0:
            print(stages[ind])
            boolean=False
            print("You lose the game")
    print("".join(blank))
    if "_" not in blank:
        boolean=False
        print("You won the game")


        


