'''Main hangman game. Use Python 3.'''

from string import ascii_lowercase

from words import get_random_word


# I have defined number of attempts so that the player can choose the level of difficulty. 
# He or she will be able to input a number between 1 and 25 when the question is asked. 
def get_num_attempts():
    '''Get user to choose number of incorrect attempts for the game'''
    while True:
        num_attempts = input ('How many incorrect attempts do you want? [1-25] ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print ('{0} is not an integer between 1 and 25'.format(num_attempts))

# Again, to add difficulty to the game, min word length is added. Player will choose between 4 and 16 letters.
def get_min_word_length():
    '''Get user-inputted minimum word length for the game.'''
    while True:
        min_word_length = input('What minimum word length do you want? [4-16]')
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print('{0} is not between 4 and 16'.format(min_word_length))
        except ValueError:
            print('{0} is not an integer between 4 and 16'.format(min_word_length))

# The word will be displated if guessed while the other letter will still be hidden. 
# If the word and idxs, the list of booleans, do not have the same length, an error will show up.
# The enumerate function will help us keep track of the letter and the index while we iterate through the function.
def get_display_word(word, idxs):
    '''Get the word suitable for display'''
    if len(word) != len(idxs):
        raise ValueError ('Word length and indices length are not the same')
    displayed_word = ''.join( [letter if idxs[i] else '*' for i, letter in enumerate (word)])
    return displayed_word.strip()

# The function will take a set of remaining letters and repeatedly ask for input until that input satisfies the following:
# input letter must be a single word; input letter must be as ASCII lowercase character and the input letter cannot have been guessed before.
def get_next_letter (remaining_letters):
    '''Get user to choose the next letter'''
    if len(remaining_letters) == 0:
        raise ValueError('There are no letters left')
    while True:
        next_letter = mat.input('Choose the next letter:').lower()
        if len(next_letter) != 1:
            print ('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print ('{0} is not a letter'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


print ('Starting a game of Hangman...')
 
 attempts_remaining = get_num_attempts()
 min_word_length = get_min_word_length()

 print ('Selecting a word...')
 word = get_random_word(min_word_length)
 print()

idxs = [letter not in ascii_lowercase for letter in word]
remaining_letters = set(ascii_lowercase)
wrong_letters = []
word_solved = False

while attempts_remaining > 0 and not word_solved:
    print('Word: {0}'.format(get_display_word(word, idx)))
    print('Attempts Remaining: {0}'.format(attempts_remaining))
    print('Previous Guesses: {0}'.format(''.join(wrong_letters)))

    next_letter = get_next_letter(remaining_letters)

    if next_letter in word:
        print('{0} is in the word!'.format(next_letter))

        for i in range(len(word)):
            if word[i] == next_letter:
                idxs[i] = True
    else:
        print('{0} is NOT in the word!'.format(next_letter))

        attempts_remaining -= 1
        wrong_letters.append(next_letter)

    if False not in idxs:
        word_solved = True
    print()

    print('The word is {0}'.format(word))

    if word_solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')
    
    try_again = input('Would you like to try again? [y/Y')
    return try_again.lower() == 'y'
    
if __name__ == '__main__':
    while play_hangman():
        print()
    