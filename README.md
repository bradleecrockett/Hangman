# Hangman
In this lab you will write a program `hangman.py` in which you play hangman against the computer. Your `hangman.py` program shall meet the following requirements.

1) Store a secret word in the variable `secret_word`. This is already done for you.

1) Display the user's progress towards guessing the secret word.
    1) To start, a blank line (an underscore) for each letter in secret word.
    1) As the game goes on, correct guesses will fill the appropriate positions in the word.
        1) For example if the secret word was "wrestle" and the user had guessed an 'e', 's' and a 't', the display would be "_ _ e s t _ l e". 
    1) Display an ASCII art representation of the hangman gallows. (Draw the hangman guy.)
        1) A completed hangman gallow has six (6) body parts: head, body, right arm, left arm, left leg and right leg. No more. This limits the number of incorrect guesses.
1) Allow the user to repeatedly guess a letter until the game is over.
    1) Determine whether the guess was in the secret word
        1) If the letter is in the secret word, place it into its appropriate spot in the user's progress.
        1) If the letter is not in the secret word, the next version of the hangman gallows should be displayed and the incorrect guess added to a missed guesses bank.
        1) If the letter was already guessed, the player should not be penalized for guessing that letter again. In other words, the hangman should remain at the same state and the player should simply get to guess again.
1) The game should have one of two possible endings.
    1) If the user was able to guess every letter in the secret word, they win and should be congratulated.
    1) If the user was unable to guess every correct letter, they lose and the entire Hangman should be displayed with a message to the user along with the secret word revealed.
    1) After either game ending, the program should ask the user if they want to play again. 
        1) If they respond yes, call the `main()` function again to restart the game.
        1) If they respond no, display a goodbye message.

