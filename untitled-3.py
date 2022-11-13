# word puzzle game version 3
# The game requires players to guess a letter of a word
def is_word_found(puzzle, answer):
    set1 = set(puzzle)
    set2 = set(answer)
    if set1 <= set2:
        return True
    else:
        return False
def display_result():
    quit = input('Press enter to end the game')
def update_puzzle_string(puzzle, answer):
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
    infile = open(filename)
    instructions = infile.read()
    infile.close()
    print(instructions)
 
def chooseWord(wordlist):
    wordlist= ['apple','banana','watermelon','kiwi','pineapple','mango']
    return random.choice(wordlist)

def play_game(puzzle):
    length = '_ ' * len(puzzle)
    result = 'The answer so far is'
    print(result + length)
    time_remain = 0
    answer = ""
    while not is_word_found(puzzle, answer) and (4-time_remain):
        ans = input("Guess a letter. (" "{}".format(4-time_remain) + ' guesses remaining)' ).lower()
        if ans not in answer:
            answer += ans
            if ans in puzzle:
                print(result,update_puzzle_string(puzzle, answer))
            else:
                print(result,update_puzzle_string(puzzle, answer))
                time_remain += 1
            
    if is_word_found(puzzle, answer):
        print("Good job, you found the word " + puzzle)
    elif time_remain == 4:
        print('Not quite, the correct word was ' + puzzle +'. Better luck next time')
    return

def main():
    display_instructions('instructions.txt')
    puzzle = chooseWord('wordlist').lower() 
    play_game(puzzle)
    display_result()
main()