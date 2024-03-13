height=int(input("Enter your height = "))
if height>120:
    print("Can Ride")
    age=int(input("Enter your age = "))
    photos=input("Do your want photos = ")
    if age<12:
        if  photos=="yes":
            print("Please pay $7")
        else:
            print("Please pay $5")
    elif age>=12 and age<=18:
        if photos=="yes":
            print("Please pay $10")
        else:
            print("Please pay $7")
    else:
        if photos=="yes":
            print("please pay $15")
        else:
            print("Please pay $12")
else:
    print("Can't Ride")
    