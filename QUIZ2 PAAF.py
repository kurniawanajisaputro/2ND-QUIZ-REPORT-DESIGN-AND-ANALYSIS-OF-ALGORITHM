# Simulate (or actually play) Guess the Number
#   The number lies in a given range. Choose the number in the middle.
#   If guess was too high, choose number in middle of lower half,
#   if guess was too low,  choose number in middle of upper half.
#   Halve the appropriate range and repeat unti the number is correct.
binary=False                    # set this to True or False
lonum,hinum=1,128               # range for the number
 
import random as r
 
the_num=r.randint(lonum,hinum)  # computer chooses a number randomly
print("I'm thinking of a number between",lonum,"and",hinum)
 
lo=1
hi=hinum
guesses=0
 
for i in range(lonum,hinum):    # repeat this until guess is correct:
                                    # note the int!
#    guess=int(input ("What is your guess: ")) # if you want to play 2 players, just uncomment this
    if binary:  guess=lo+(hi-lo)//2     # integer division
    else:       guess=r.randint(lo,hi)
   
    guesses+=1                     # add 1 to count of guesses
    Input1 = input ("Enter your number")
    print("Guess:",guess)
    Number = int(Input1)
    # check the guessed number
    if guess > the_num:
        
        hi=guess
             # bring down the upper bound
    elif guess < the_num:
        
        lo=guess      # push up the lower bound
        
    elif guess == the_num:
        print("That took",guesses,"guesses,You lose!!!" )
        break
    else : guess == guess+1                # yay!
    if Number > the_num:
        print("Lower!")           
    elif Number< the_num:
        print("Higher!")
    elif Number== the_num:
        print("That took",guesses,"guesses,You win!!!" )
        break
#    else: break
        
 

#print("That took {0} guesses".format(guesses)) # alternative to previous line
