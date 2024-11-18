'''
Hangman game
Objectives:
- A word is choosen randomly from the list of "words"
- the player guesses letters to figure out the hidden word
- The player has a limited number of attempts to guess the word
- The Hangman's drawing is completed(changes) with every wron letter guessed
- potential errors are handled
'''


import random

words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
    'compiler', 'database', 'encryption', 'firewall', 'hardware',
    'internet', 'java', 'kernel', 'malware', 'network', 'object',
    'protocol', 'query', 'router', 'security', 'token', 'url',
    'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract', 'binary',
    'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
    'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node']

hangman_stages = ["""
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]


chosen_word = random.choice(words)    # Choose a word at random from the list
print(chosen_word)

word_display = ['_' for _ in chosen_word]

attempts = 6    # Maximum number of guesses allowed

print("Welcome to Hangman!")


# Function to display the current state of the word and the hangman
def display_state():
    print(f"attempts = {attempts}")
    print(hangman_stages[attempts])
    print(' '.join(word_display))


def display_word():
    print(' '.join(word_display))


while attempts > 0 and '_' in word_display:
    display_state()
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                if word_display[index] == '_':  # Check if the letter hasn't already been revealed
                    word_display[index] = guess
    else:
        print("Incorrect. Try again.")
        attempts -= 1

    # Check for win condition
    if '_' not in word_display:
        display_state()
        print("Congratulations, you won!")
        break

# If the loop ends because of running out of attempts
if attempts == 0:
    display_state()
    print("Sorry, you lost. The word was:", chosen_word)

display_word()
