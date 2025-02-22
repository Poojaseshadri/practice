#if condition
a=int(input("Enter a number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")

a = int(input("Enter a number: "))  
if a != 0:
    if a > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
else:
    pass  
#while loop
a = 0  
while a < 10:  
    a += 1 
    if a == 3:  
        continue  
    if a == 7:  
        break  
    print(a)   
else:  
    pass  
#for loop

for a in range(1, 10):  
    if a == 3:  
        print(a)
        continue  
    if a == 7:  
        print(a)
        break  
    print(a)   
else:  
    print(a)  
    
#function
def check_even_odd(a):  
    if a % 2 == 0:  
        print(a, "is Even")  
    else:  
        print(a, "is Odd") 
check_even_odd(5)  
check_even_odd(8)

#lambda
x = lambda a, b, c : a + b + c  # noqa: E731
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n
function=myfunc(2)
print(function(5))

