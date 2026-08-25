# GUESS THE NUMBER ---- >

print("If your choiced value is same as the computer chosen then you will be a winner !!!")


# Selection if range -- >

rng = int (input("Select range = "))

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

attempt = 1

n = int (input ("No. of attempts (max-'10')= "))

user_choice = int(input("Select any random number = "))



# Condn of winning -- >

while True :
    if (rng <= 0) :
        print ("Invalid ")
        break

    elif ((n>10) or (n<=0)) :
        print (f"Invalid attempt!")
        break
    
    elif (comp_choice == user_choice) :
        print(f"Hurrah ! You win the game at {attempt}")
        break
    elif ((user_choice) > rng or (user_choice < 1)):
        print(f"Invalid number!")
        break
    elif (comp_choice > user_choice) :
        
        attempt += 1
        if (attempt > n ) :
                    print (f"You did'nt complete your game in {n} attempts!")
                    break 
        print(f"Choose greater value")
        user_choice = int(input("Try again = "))
    elif (comp_choice < user_choice) :
        
        attempt += 1
        if (attempt > n ) :
                            print (f"You did'nt complete your game in {n} attempts!")
                            break 
        print(f"Choose smaller value")
        user_choice = int(input("Try again  = "))

print (f"computer choosed = {comp_choice}")
print("---GAME OVER---")
    
        
    
    


        
                                       
