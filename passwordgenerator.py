import sys
import random
print("\t\t\t\t\t\t\t\t\t\tWELCOME TO PASSWORD GENERATOR")
l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     '!','@','#','$','%','^','&','*','(',')','-','+'
     '1','2','3','4','5','6','7','8','9','0']
def generate():
    x = int(input("Input length of password required : "))
    p=''
    for i in range(x):
        p = p + random.choice(l)
    print("Generated password : ",p)
    b = input("Enter R or r to regenerate password ; Enter E or e to exit : ")
    if b=='R' or b=='r':
        generate()
    if b=='E' or b=='e':
        sys.exit()
generate()
