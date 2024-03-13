#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

#creating a number guessor class
 

class number_guessor:

    def __init__(self, number_of_guesses = 0):

        self.number = random.randint(1,10)

        print(self.number)

        self.number_of_guesses = 4

        self.player_name = input ("Please enter your name: ")

        self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

       
      
  

        if self.player_guess == self.number:

            return print("Congratulations: You got the right answer")

   

        
   

    

             

    
           
        #to prevent player from inputting an invalid number:

        if self.player_guess >10 or self.player_guess <= 0:

                    print("You have entered an invalid number; please try again")

        #to begin the loop for giving hints         

        while self.player_guess!= self.number:
            self.number_of_guesses -= 1
            if self.number_of_guesses == 0:
                print ("You have reached the maximum number of guesses")
                
                break
            
            hint = input("You have guessed an incorrect number.Would you like to have a hint? Please enter [a,b or c] in the terminal")
            
            if True:
             # hint b is if the player guessed the number too high or too low                
                if hint =="b" and self.player_guess>self.number: 

                    print("You guessed a number too high")
                    
                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))
                    
                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")
                    
                elif hint =="b" and self.player_guess<self.number:
                    print( "You guessed a number too low"  )
                    
                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))
                    
                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")
             
                # hint c is if player guessed an even number instead of odd; or an odd number instead of even
                # hint c is also if player guessed an incorrect even number or an incorrect odd number..
                
                elif hint == "c" and self.number%2 == 0 and self.player_guess%2!=0:
                    print ("You've guessed an odd number instead of an even number")

                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")


                elif hint == "c" and self.number%2!=0 and self.player_guess%2==0:
                    print ("You've guessed an even number instead of odd number")

                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")
                
                elif hint == "c" and self.number%2 != 0 and self.player_guess%2!=0:
                    print ("You've guessed an odd number; but just not the right odd number")

                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")


                elif hint == "c" and self.number%2==0 and self.player_guess%2==0:
                    print ("You've guessed an even number; but not the right even number")

                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")
    # hint a is to provide the player with multiples of the correct answer.
                elif hint =="a":
                    for i in range (1,10):
                        if self.number%i == 0:
                            print (f"Correct Answer is a multiple of {i}")
                            
                    self.player_guess = int(input(f"{self.player_name}, please guess a number between 1 and 10. You have four guesses"))

                    if self.player_guess == self.number:

                        return print("Congratulations: You got the right answer")

                else:
                    break 
            
                
          
                 
                 
               
program = number_guessor() 


# In[ ]:





# In[ ]:




