# GUESS THE NUMBER ---- >

num_list = []

for i in range (1,101) :
    num_list.append(i)
    i += 1

# Computer chosen value -->
import random 

def comp_fn () :
    return random.choice(num_list)

comp_choice = comp_fn ()

# user input -- >

print("If your choiced value is same as the computer chosen then you will be a winner !!!")
user_choice = int(input("Select any random number in range(1-100) = "))

attempt = 0

# Condn of winning -- >

while True :
    attempt += 1
    if (comp_choice == user_choice) :
        print(f"Hurrah ! You win the game at {attempt} attempt as computer also choosed {comp_choice}  ")
        break
    elif (user_choice > 100):
        print(f"Entered value is greater than 100 which is not in range of 1-100.Restart the game !!!")
        break
    elif (user_choice < 1):
        print(f"Entered value is smaller than 1 which is not in range of 1-20.Restart the game !!!")
        break
    elif (comp_choice > user_choice) :
        print(f"Oops! your chosen value is smaller than computer choosen value.So choose that value which is greater than {user_choice}")
        user_choice = int(input("Now choose that value which should be greater than your previous value = "))
    elif (comp_choice < user_choice) :
        print(f"Oops! your chosen value is greater than computer choosen value.So choose that value which is smaller than {user_choice}")
        user_choice = int(input("Now choose that value which should be smaller than your previous value = "))
    
print("---GAME OVER---")
    
        
    
    


        
                                       
