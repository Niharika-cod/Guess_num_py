# GUESS THE NUMBER ---- >

print("If your choiced value is same as the computer chosen then you will be a winner !!!")


# Selection if range -- >

rng = int (input("Select range(assuming starting value is 1) = "))

num_list = []

for i in range (1,(rng+1)) :
    num_list.append(i)
    i += 1

# Computer chosen value -->
import random 

def comp_fn () :
    return random.choice(num_list)

comp_choice = comp_fn ()

# user input -- >



n = int (input ("No. of attempt you challenge the computer to win = "))

user_choice = int(input("Select any random number in your range = "))

attempt = 0

# Condn of winning -- >

while True :
    attempt += 1
    if (attempt > n ) :
        print (f"You did'nt complete your game in {n} attempts!")
        break 
    elif (comp_choice == user_choice) :
        print(f"Hurrah ! You win the game at {attempt} attempt as computer also choosed {comp_choice}  ")
        break
    elif (user_choice > rng):
        print(f"Entered value is not in range of {rng}.Restart the game !!!")
        break
    elif (user_choice < 1):
        print(f"Entered  is not in range of {rng}.Restart the game !!!")
        break
    elif (comp_choice > user_choice) :
        print(f"Oops! your chosen value is smaller than computer choosen value.")
        user_choice = int(input("Try again = "))
    elif (comp_choice < user_choice) :
        print(f"Oops! your chosen value is greater than computer choosen value.")
        user_choice = int(input("Try again  = "))
    
print("---GAME OVER---")
    
        
    
    


        
                                       
