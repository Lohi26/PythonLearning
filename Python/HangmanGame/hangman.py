#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


index=random.randint(0,len(word_list)-1)
word=word_list[index]
print(word)

blank=["_"]*len(word)
boolean=True
lives=0

while boolean:
    user=input("Guess a letter....!!\n")
    letter_list=list(word)
    for i in range(len(letter_list)):
        if user==letter_list[i]:
            blank[i]=blank[i].replace("_",user)
            if "_" in blank:
                boolean=True
            else:
                boolean=False
    lives+=1
    if lives==6:
        boolean=False
print(blank)
        


