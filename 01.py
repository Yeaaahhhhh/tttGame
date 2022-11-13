# word puzzle game version 3
# The game requires players to guess a letter of a word
def is_word_found(puzzle, answer):
# Determines if the player has guessed all the letters in the puzzle or not;
# - puzzle is a list representing the puzzles current state;
#return: a boolean indicating if all the letters have been guessed;    
    set1 = set(puzzle)
    set2 = set(answer)
    if set1 <= set2:
        return True
    else:
        return False
def get_guess(puzzle, answer):
    str1 = ""
    for i in range(len(puzzle)):
        str1 += "_ "
    ls = str1.split(" ")
    str1 = ""
    for it in answer:
        if it in puzzle:
            ls[puzzle.index(it)] = it
            try:
                ls[puzzle.index(it,puzzle.index(it)+1)] = it
                ls[puzzle.index(it,puzzle.index(it)+1)] = it
                ls[puzzle.index(it,puzzle.index(it)+1)] = it
            except:
                pass

    for item in ls:
        str1 += item
        if item == "_":
            str1 += " "
    return str1

 
import random
def display_instructions(filename):
# Display the instructions for the game
# -filename is the name of a file from which instructions are read and then displayed to screen.
    infile = open(filename)
    instructions = infile.read()
    infile.close()
    print(instructions)
 
def chooseWord(wordlist):
    wordlist= ['apple','banana','watermelon','kiwi','pineapple','mango']
    return random.choice(wordlist)
 
class Game(object):
    def __init__(self,puzzle):
        length = '_ ' * len(puzzle)
        result = 'The answer so far is'
        print(result + length)
        global time_remain
        time_remain = 0
        global answer
        answer = ""
        while not is_word_found(puzzle, answer) and (4-time_remain):
            a = input("Guess a letter. (" "{}".format(4-time_remain) + ' guesses remaining)' )
            if a not in answer:
                answer += a
                if a in puzzle:
                    print(result,get_guess(puzzle, answer))
                else:
                    print(result,get_guess(puzzle, answer))
                    time_remain += 1
    def __call__ (self, puzzle):
        if is_word_found(puzzle, answer):
            print("Good job, you found the word " + puzzle)
        elif time_remain == 4:
            print('Not quite, the correct word was ' + puzzle +'. Better luck next time')
        return
    
def main():
    display_instructions('instructions.txt')
    global puzzle
    puzzle = chooseWord('wordlist').lower()
    p = Game(puzzle)
    p(puzzle)
    quit = input('Press enter to quit the game')
main()
