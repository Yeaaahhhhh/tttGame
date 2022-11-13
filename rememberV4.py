# Remember The Word Version 4
# This game displays 4 words to the player and ask the player to recall one of the words

# Addressing the Software Quality Issue of Non-Adjacent Duplicate Line Groups
# Look at clear screen and display header occurs 3 times in our code
# Solution - define a function once that will do this task
        # - call the function multiple time promotes resuse.

# Modularization - break up and organize the code based on the task it executes
# Practice Problem decomposition - Decompose the problem into single well-defined tasks. 
# Each well defined task is completed by a user defined function 
# Advantage 1 - task division amongst mutlitple programmers working on large complex programs 
# Advantage 2 - locating and fixing an error in the program becomes easier
# Advantage 3 - making changes to the program is also easier 
import time,os,random

def display_instructions():
    # displays the instructions in the program
    filename = 'instructions.txt'
    infile = open(filename)
    instructions = infile.read()
    # <identifier>.<method>()
    instructions = instructions.strip()
    print(instructions)    

def display_header():
    # clearing the screen and displaying the header
    # Software Quality Issue - Repeated literals  - replace with identifiers
    clear_command = 'cls'
    header_border = '-' * 80
    header_content = 'Guess The Word' 
    os.system(clear_command) # os.system('cls') for Windows
    print(header_border)
    print(header_content)
    print(header_border)    

def sample_words():
    # choosing 4 words from a list of words
    # returning the list of words
    # CALLEE
    file = open('words.txt','r')
    # file is bound to an object whose type is TextIOWrapper just like str
    # we used the lower method in str
    # we can use the read method on the TextIOWrapper class
    # A method is a function inside a class -- <identifier>.<method_name>()
    content = file.read()
    # content will have new line characters 
    all_words = content.splitlines() # content is turned into a list of words
    # list is type in Python
    # sequences are containers that can hold more than one object inside it
    # length of a sequence len(<identifier>) - len(words)--> 4
    # access an object inside a list - <identifer>[<index>] - words[1] - chair
    #words = ['orange','chair','mouse','sandwich']
    words_to_show = 4
    words = random.sample(all_words,words_to_show)
    return words # throw

def display_words(word_list):
    # display the words from a list of words
    # parameter - words
    
    # the parameter is bound to the object the argument is bound to
    # name of the parameter does not have to be the same as the name of the argument
    
    # Duplicate Adjacent Line Groups - iterative - for, while
    pause_time = 2
    for word in word_list:
        print(word)
        time.sleep(pause_time)
        display_header() 
    # no return from this function
    # this function returns a None object whose type is NoneType
    
    
    
def main():
    continue_game = True
    while continue_game == True:
        # BLOCK Display the header
        display_header()
        
        # BLOCK Display the instructions
        display_instructions()
        
        # Player is prompt to press
        input('Press enter to display the words')
        
        # BLOCK Display Header
        display_header()  
        
        # BLOCK Sample words
        words = sample_words() # catch
        # Choose the correct answer randomly
        correct_answer = random.choice(words)
        # correct_answer is a string
        # str is a sequence of characters
        start_letter = correct_answer[0]
        
        # BLOCK Display Words
        display_words(words) # words is called the argument - order placed at the drivethrough  
        
        # Alternate Way - accessing the items using the position of the item
        # position ---> 0,1,2,3
        # range(0,4) or range(4)
        # sequences -- str,list,range    
        #for index in range(0,4):
            #print(words[index]) # access the object in the list using its position
            #time.sleep(2)
            ## clear the screen
            #os.system(clear_command)
            ## Display the header
            #print(header_border)
            #print(header_content)
            #print(header_border)    
        
                
        # BLOCK - Prompt the play to enter a word
        guess=input('What word begins with the letter '+start_letter+'?')
        
        # BLOCK - display feedback
        # Methods - functions that exist inside a class
        # Type - Class
        # Calling a method --->  <identifier>.<method>()
        if guess.lower() == correct_answer:
            print('Congratulations , you are correct.')
        else:
            print('Sorry , you entered '+ guess + '.')
        print('The answer was '+correct_answer+'.')
        
        # BLOCK - Prompt the player to play again
        response = input('Play Again (y/N)?')
        # Absence of return statement means the function is returning a None object
        if response.lower() != 'y': # != not equal == equality
            continue_game = False

        
main()