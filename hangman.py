# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    counter = 0
    for index in range(len(secret_word)):
        for char in letters_guessed:
            if secret_word[index] == char:
                counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = secret_word
    x = word
    for index in range(len(secret_word)):
        for i in range(len(letters_guessed)):
            if secret_word[index] == letters_guessed[i]:
                break
            if i == len(letters_guessed)-1 and secret_word[index] != letters_guessed[i]:
                word = list(word)
                word[index] = "_ "
                x = "".join(word)
    
    return x



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    new_character = string.ascii_lowercase
    new_character = new_character.translate({ord(i): None for i in letters_guessed})
    return new_character
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = ""
    warning = 3
    s = set(secret_word)
    print("Welcom to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have", warning, "warnings left.")
    print("-------------")
    for t in range(6, 0, -1):
        
        while True:
            f = 0
            print("You have", t, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            letters_guessed += input("Please guess a letter: ")
            if(str.isalpha(letters_guessed[len(letters_guessed)-1])):
                str.lower(letters_guessed)
                
                
                
                for z in range(len(letters_guessed)-1):
                    if letters_guessed[z] == letters_guessed[len(letters_guessed)-1]:
                        f += 1
                        break
                    
                if f > 0:
                    warning -= 1
                    if warning < 0:
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                        break
                    print("Oops! You've already guessed that letter. You now have", warning, "warnings:", get_guessed_word(secret_word, letters_guessed))
                    print("-------------")
                    
                    continue
                

                d = 0
                for char in secret_word:
                    if letters_guessed[len(letters_guessed) - 1] == char:
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                        print("-------------")
                        d += 1
                        break
                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations, you won!")
                    total_score = t * len(s)
                    print("Your total score for this game is:", total_score)
                    break
                if(d == 0):
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    print("-------------")
                    break
            else:
                warning -= 1
                print("Oops! That is not a valid letter. You have", warning , "warnings left:",get_guessed_word(secret_word, letters_guessed))
                print("-------------")
            if warning < 0:
                 print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                 print("-------------")
                 break
        if is_word_guessed(secret_word, letters_guessed):
            return
    print("sorry, you ran out of guesses. The word was", secret_word)
            
            
        
            
            
        
    
                
            
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_stripped = my_word.replace(" ", "")
    same_char = []
    blank_stripped = []
    if len(my_word_stripped) != len(other_word):
        return False
    for index, letter in enumerate(my_word_stripped):
        if letter in string.ascii_lowercase:
            same_char.append(index)
        else:
            blank_stripped.append(index)

    mws = ''
    ow = ''
    for index_same in same_char:
        for index_dif in blank_stripped:
            if other_word[index_dif] == other_word[index_same]:
                return False
            mws += my_word_stripped[index_same]
            ow += other_word[index_same]
    
    return mws == ow
        
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    possible_matches = [i for i in wordlist if match_with_gaps(my_word, i)]
    return ' '.join(possible_matches)
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = ""
    warning = 3
    s = set(secret_word)
    print("Welcom to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have", warning, "warnings left.")
    print("-------------")
    for t in range(6, 0, -1):
        
        while True:
            f = 0
            print("You have", t, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            letters_guessed += input("Please guess a letter: ")
            if letters_guessed[len(letters_guessed)-1] == '*':
               print (show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            elif str.isalpha(letters_guessed[len(letters_guessed)-1]):
                str.lower(letters_guessed)
                
                
                
                for z in range(len(letters_guessed)-1):
                    if letters_guessed[z] == letters_guessed[len(letters_guessed)-1]:
                        f += 1
                        break
                    
                if f > 0:
                    warning -= 1
                    if warning < 0:
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                        break
                    print("Oops! You've already guessed that letter. You now have", warning, "warnings:", get_guessed_word(secret_word, letters_guessed))
                    print("-------------")
                    
                    continue
                

                d = 0
                for char in secret_word:
                    if letters_guessed[len(letters_guessed) - 1] == char:
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                        print("-------------")
                        d += 1
                        break
                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations, you won!")
                    total_score = t * len(s)
                    print("Your total score for this game is:", total_score)
                    break
                if(d == 0):
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    print("-------------")
                    break
            else:
                warning -= 1
                print("Oops! That is not a valid letter. You have", warning , "warnings left:",get_guessed_word(secret_word, letters_guessed))
                print("-------------")
            if warning < 0:
                 print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                 print("-------------")
                 break
        if is_word_guessed(secret_word, letters_guessed):
            return
    print("sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
