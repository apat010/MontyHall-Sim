import random 
import time
start_time = time.time()
#Used to measure time taken to execute program 
def create_doors(): 
    doors = [False for i in range(3)]
    Prize_door = random.randint(0,2)
    doors[Prize_door] = True 
    return doors 
    # Makes 2 of the Doors False, while one is True 

def selected_door(doors):
    return random.choice(doors) 

# Choose one of the doors at Random

def Round():
    doors = create_doors()
    picked_door = selected_door(doors)
    if picked_door is True :
        return 0
    else: 
        return 1
# Determines whether switching or staying resulted in win or loss 

def main_function():
    Good_Change = 0
    Total_Rounds = 1000000
    
    for i in range(Total_Rounds):
        Good_Change += Round()
        Bad_switch = Total_Rounds - Good_Change
    print("Wins after switching:",Good_Change)
    print(f"Total Trials:",Total_Rounds)
    print(f"Probability of winning after switch: {Good_Change*100/Total_Rounds:} Percent")
    print("Loses after switching:",Bad_switch)
    print(f"Experiment Completed in: {round(time.time()-start_time,5)} Seconds")
main_function()