#Prime number program



n=int(input("Enter the number to be checked="))

def prime(n):
    flag=0
    if n==1 or n==0:
        return "Neither prime nor composite"
    for i in range(2,int(n/2)+1):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return "It is prime number"
    else:
        return "It is not a prime number"
print(prime(n))    