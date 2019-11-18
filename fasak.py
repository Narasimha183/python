print("fasak 1234567890")

num1 = input("enter the number :")
num2 = int(num1)
count = 0
for x in range(1,num2+1) :
    if num2%x==0 :
        count = count+1
    else :
        count = count
if count==2 :
    print("given number is prime")
else :
    print("given number is not a prime")
    
    
num1 = input("enter the number :")
num2 = int(num1)
for x in range(1,num2+1) :
    for y in range(1,x+1) :
        print (x,end="")
    print("\r")
 
 
num1 = input("enter the number :")
num2 = int(num1)
for x in range(1,num2+1) :
    for y in range(1,x+1) :
        print (y,end="")
    print("\r")
    
#print prime numbers between interval    
num1=int(input("enter the starting number"))
num2=int(input("enter the ending number"))
for x in range(num1,num2+1) :
    count = 0
    for y in range(1,x+1) :
        if x%y == 0 :
            count = count+1
    if count == 2 :
        print(x)
        
 #fibonic series
num1 = int(input("enter the number"))
a =0
b = 1
print(a)
print(b)
for x in range(3,num1+1) :
    c = a+b
    a = b
    b = c
    print(c)
 
 
 #prime number using function AND PASSING THE ARGUMENTS
 
 def function1(x) :
    count = 0
    for y in range(1,x+1) :
        if x%y == 0 :
            count = count+1
    if count == 2 :
        print("given number is prime")
    else :
        print("not a prime")

function1(10)



#sum of array

a=[1,2,3,4,5,6,7,8,9,10]
b=len(a)
sum = 0
for x in range(0,b) :
    sum = sum+a[x]

print(sum)

#factorial of given number
num1=int(input("enter the number for finding the factorial"))
count = 1
for x in range (1,num1+1) :
    count = count*x
print(count)



#given is fibonaic or not
num1 = int(input("enter the number to be checked"))
def function1(x) :
    a = 0
    b = 1
    for x in range (1,x+1) :
        c = a+b 
        a=b
        b=c
        if c==num1 :
            print("given number is fabonic")
            break 
        
        
function1(100)

#max no of array 
def max_ar() :
    arr=[1,2,3,4,5,6,7,8,9,11,15,1,6,45,2324]
    max1 = arr[0]
    b = len(arr)
    for x in range (1,b) :
        if arr[x] > max1 :
            max1 = arr[x]
    return max1

print(max_ar())


#guessing game in number and try for string
gue=int(input("choose the number for guessing from 0 to 99"))
userguess=""
while userguess!=gue :
    userguess=int(input("choose the number for guessing from 0 to 99"))
    if userguess<gue :
        print("your number is lessthan guess number")
    if userguess>gue :
        print("your number is greaterthan guess number")
    if userguess==gue :
        print("guess number is coreect and you won")


#sum of squares of n natural numbers
n = int(input("enter the number"))
sum1 = 0
for x in range (1,n+1) :
    sum1 = sum1+(x*x)

print(sum1)


#sum of cubes of n natural numbers
n = int(input("enter the number"))
sum1 = 0
for x in range (1,n+1) :
    sum1 = sum1+(x**3)

print(sum1)






