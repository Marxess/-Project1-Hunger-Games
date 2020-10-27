import random
# Wordlist contains 69000 words. I downloaded from a link and stored it in a file called wordlist.txt
WORDLIST = 'wordlist.txt.rtf'

# The function below will extract a random word from the wordlist created
def get_random_word(min_word_length):
    """Get a random word from the wordlist using no extra memory."""
    words = []
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' or ')' in word:
                continue  # Skip the word because it contains parentheses.
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue  # Skip the word because it is too short.
            words.append(word)
    return random.choice(words)

def play_hangman():
    '''Play the hangman game. At the end of the game, returns if the player wants to retry.'''
