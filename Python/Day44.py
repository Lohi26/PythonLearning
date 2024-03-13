import random
names="Angela, Ben, Jenny, Michael, chloe"
str=names.split(", ")
a=random.randint(0,len(str)-1)
print(f"{str[a]} is going to buy the meal today!")