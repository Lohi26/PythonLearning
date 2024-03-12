

# height=int(input("Enter your height = "))
# if height>120:
#     print("Can Ride")
#     age=int(input("Enter your age = "))
#     if age>18:
#         print("Pay 12 dollars")
#     else:
#         print("Pay 7 dollars")
# else:
#     print("Can't Ride")


height=int(input("Enter your height = "))
if height>120:
    print("Can Ride")
    age=int(input("Enter your age = "))
    if age<12:
        print("Please pay 5 dollars")
    elif age>=12 and age<=18:
        print("Please pay 7 dollars")
    else:
        print("Please pay 12 dollars")