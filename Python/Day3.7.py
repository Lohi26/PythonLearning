size=input("Enter the size of the pizza (S or M or L) =")
add_pepperoni=input("Enter Yes or no (Y or N) = ")
extra_cheese=input("Enter Yes or no (Y or N) = ")
small=15
medium=20
large=25
peps=2
pepm=3
extraCheese=1
amount=0
if size=="S":
    amount+=small
    if add_pepperoni=="Y":
        amount+=peps
    if extra_cheese=="Y":
        amount+=extraCheese
elif size=="M":
    amount+=medium
    if add_pepperoni=="Y":
        amount+=pepm
    if extra_cheese=="Y":
        amount+=extraCheese
else:
    amount+=large
    if add_pepperoni=="Y":
        amount+=pepm
    if extra_cheese=="Y":
        amount+=extraCheese
print("Thank for choosing Python Pizza! 🍕")
print(f"Your final bill is ${amount}")    