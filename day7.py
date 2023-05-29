

import random as rr
word_list=["ardvark","baboon","camel"]
chosen_word=rr.choice(word_list)
print(f"chosen word is: {chosen_word}")



display=[]
for letter in chosen_word:
    display+="_"
print(display)


lives=6
game=False

while not game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        game = True
        print("You win.")

    







