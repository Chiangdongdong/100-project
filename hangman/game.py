import random
import hangman_art
import hangman_word

chosen_word = random.choice(hangman_word.word_list)    #variable
word_length = len(chosen_word)
end_of_game = False
lives = 6


display = []                        #important lists
for letter in range(word_length):          
 display += "_"

answer_list = []
for i in chosen_word:
  answer_list.append(i)

stage = hangman_art.stages

print(hangman_art.logo)          #game
print(f"{' '.join(display)}")
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  for position in range(word_length):           #right guess
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter 
  
  if "_" not in display:        #right guess to win
    end_of_game = True
    print("You win!")
  
  elif guess not in answer_list:      #wrong guess 
    lives -= 1
    print(stage[lives]) 
    
    if lives == 0:                #wrong guess to lose
      print("You lose.")
      end_of_game = True
     
  print(f"{' '.join(display)}")
if end_of_game == True:
  print(f"The answer is {chosen_word}.")