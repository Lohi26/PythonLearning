#Love calculator


print("The love calculatore is calculating your score......")
name1=input("Enter your name = ")
name2=input("Enter your partner's name = ")

name=(name1+name2).lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")

l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")

first=str(t+r+u+e)
second=str(l+o+v+e)

level=first+second

if int(level)<10 and int(level)>90:
    print(f"Your score is {level} you both go together like coke and mentos")
elif int(level)>40 and int(level)<50:
    print(f"Your score is {level}, you both are alright together")
else:
    print(f"Your score is {level}")