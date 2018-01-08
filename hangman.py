import random


HANGMAN = [
    """
        ---
       |   |
       |
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       |
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       |  -+-
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |
       |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |  |
       |  |
       |
    --------
    """,
    """
        ---
       |   |
       |   0
       | /-+-\\
       |   |
       |   |
       |  | |
       |  | | 
       |
    --------
    """]
    

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("COYOTE", "MONSTER", "CANTELOPE", "GRADUATION", "HANGMAN")
word = random.choice(WORDS)
#print word
so_far = "-" * len(word)

wrong = 0
used = []
#print so_far

print "Welcome to Hangman, Good luck!"

while wrong < MAX_WRONG and so_far != word: #-->> 5th
    
    print HANGMAN[wrong]
    print "You've used the following letters: " , used
    print "So far, the word is", so_far
    
    #getthe players guess  ->>> 1st
    guess = raw_input("Enter your guess: ")
    guess = guess.upper()

    while guess in used: #-->>> 2nd
        print "You've already guessed the letter:" , guess
        guess = raw_input("Enter your guess: ")
        guess = guess.upper()
    used.append (guess)

    #check the guess   -->>>> 3rd 
    if guess in word:
        print "\nYes!", guess, "is in the word!"
        new = ""
        for i in range(len(word)): #-->> 4th
            
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print "\nSorry", guess, "isn't in the word."
        wrong += 1
     ## end the game loop
        
if wrong == MAX_WRONG:
    print HANGMAN[wrong]
    print "You have been hanged"
else:
    print "You guessed it!"
    print "The word was", word

raw_input("Press the enter key to exit")
        
