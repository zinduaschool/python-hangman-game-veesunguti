#Hangman game!
import random
#import time module
import time

#welcome player
print("Welcome to the Hangman game!")
name = input("Enter your name: ")
print ("Hello, " + name, "Let's play hangman!")

#wait a second
time.sleep(1)
print ("Start guessing...")
time.sleep(1)

#A List Of Words
words = ['python','program','gaming','coding','mutant','husky']
word = random.choice(words)
guesses = ''

#determine the number of turns
turns = 6

# while loop
while turns > 0:         
    failed = 0   

    # for loop and if analysis           
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("You won") 
        break      

    # ask player to guess a character        
    guess = input(" guess a character:") 
    guesses += guess  

    if guess not in word:  
        turns -= 1        
        print("Wrong")    
        print("You have", + turns, 'more guesses') 
        if turns == 0:           
            print ("You Lose") 