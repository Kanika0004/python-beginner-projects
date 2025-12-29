import random
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
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)

word_to_guess=""
for letter in chosen_word:
    word_to_guess+='_'
print(chosen_word)
print(f"Word to guess: {word_to_guess}")
game_over=False
correct_letters=[]
lives = 6
while not game_over:
    guess = input("Guess a letter:").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives =lives- 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over=True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
        else :
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")

    if "_" not in display:
        game_over = True
        print("You win.")