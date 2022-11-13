# Remember The Word Version 4
# This game displays 4 words to the player and ask the player to recall one of the words
import time
import os 
import random

def main():
    continue_game = True
    while continue_game == True:
        # BLOCK Display the header
        # Software Quality Issue - Repeated literals  - replace with identifiers
        clear_command = 'clear'
        header_border = '#' * 80
        header_content = 'Guess The Word' 
        os.system(clear_command) # os.system('cls') for Windows
        print(header_border)
        print(header_content)
        print(header_border)
        
        # BLOCK Display the instructions
        filename = 'instructions.txt'
        infile = open(filename)
        instructions = infile.read()
        # <identifier>.<method>()
        instructions = instructions.strip()
        print(instructions)
        
        # Player is prompt to press
        input('Press enter to display the words')
        
        # BLOCK Display Header
        # clear the screen
        os.system(clear_command)
        # Display the header
        print(header_border)
        print(header_content)
        print(header_border)    
        
        # BLOCK Sample words
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
        # Choose the correct answer randomly
        correct_answer = random.choice(words)
        # correct_answer is a string
        # str is a sequence of characters
        start_letter = correct_answer[0]
        
        # BLOCK Display Words
        # Duplicate Adjacent Line Groups - iterative - for, while
        pause_time = 2
        for word in words:
            print(word)
            time.sleep(pause_time)
            # clear the screen
            os.system(clear_command)
            # Display the header
            print(header_border)
            print(header_content)
            print(header_border)    
        
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