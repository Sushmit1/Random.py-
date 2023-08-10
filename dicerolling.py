import sys
import random
l = [1,2,3,4,5,6]
print("\t\t\t\t\t\t\t\t\t\tWELCOME TO DICE ROLLING SIMULATOR")
def roller():
    
    if a=='R' or a=='r' :
        print("Your die roll is : ",random.choice(l))
    if a=='E' or a=='e' :
        sys.exit()
    b = input("Enter R or r to roll dice ; press E or e to exit : ")
    if b=='R' or b=='r':
        roller()
    if b=='E' or b=='e':
        sys.exit()
a = input("Enter R or r to roll dice ; press E or e to exit : ")
if a=='R' or a=='r' :
        roller()
if a=='E' or a=='e' :
        sys.exit()

