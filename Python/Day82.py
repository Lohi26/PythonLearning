

def printing(name,location):
    print(name)
    print(location)

printing("Lohita","Banglore")


#Sum of the array elements...
arr=[1,2,3,4,5]
def add(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum
print(add(arr))



def add(a,b):
    print(a,b)
    return a+b
print(add(b=50,a=30))