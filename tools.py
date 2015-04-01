from random import *

def roll_1d20():
    d20_dice = randint(1, 20)
    return d20_dice
    

def roll_3d20():
    results = []
    for i in range(0,3):
        results.append(roll_1d20())
    return results    
        
