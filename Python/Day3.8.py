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
    elif age>=45 and age<=55:
        print("Everything is going to be okay. Have a free ride on us!")
        if photos=="yes":
            print("You look beautiful and it's free!")
    else:
        if photos=="yes":
            print("please pay $15")
        else:
            print("Please pay $12")
else:
    print("Can't Ride")
    