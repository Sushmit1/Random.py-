import sys
import random
p = ['It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As i see it,yes','Most likely','Outlook good','Yes','Signs point to yes',
     'Reply hazy, try again,','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Dont count on it','My reply is no',
     'My sources say no','Outlook not so good','Very doubtful']
print("\t\t\t\t\t\t\t\t\t\t\tWELCOME TO MAGIC 8 BALL")
def execute():
    q = input("Ask a question : ")
    print("Magic 8-ball : ",random.choice(p))
    c = input("Enter A to ask again or enter E to exit : ")
    if c=='A':
        execute()
    if c=='E':
        sys.exit()
    else:
        print("Incorrect Input entered")
execute()

