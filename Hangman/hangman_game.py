import random
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)


spaces = []
for _ in range(len(chosen_word)):
    spaces += '_'
print(spaces)


end_of_game = False
stage_status = 6

while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in spaces:
         print(f"You have already chosen: {guess}")
        
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
         
        if letter == guess:
            spaces[i] = guess

    if guess not in chosen_word:
         print(f"Bro! Nothing is here for '{guess}' ")
       
    if guess not in chosen_word:
        stage_status -= 1

    print(stages[stage_status])
    print(f"{' '.join(spaces)}")

    if "_" not in spaces:
        print("You won the game")
        end_of_game = True


    if stage_status == 0:
      print("You lose the game")
      end_of_game = True

