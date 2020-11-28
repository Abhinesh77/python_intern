#add 2 to list
l=[1,2,3,4,5];
print("before update\n");
for i in l:
    print(i,end="")
print("\nafter update");    
for i in l:
    i=i+2;
    print(i,end="")


#pattern
print("\npattern")    
    
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="");
    print();
print("\nfibonacci series:\n")
#fibonacci
def fib(n):
    a=-1;
    b=1;
    for i in range(0,n):
        c=a+b;
        print(c)
        a=b;
        b=c;
n=int(input("enter a number of elements to be print for fibonacci series"))
fib(n);        
        
#armstrong
print("\nAmrstrong\n");
def arm(n):
    z=list(n);
    m=[int(i) for i in z]
    y=int(n);
    x=0;
    for i in m:
        x=x+(i**3)
    if(x==y):
        print(f"{y} is an armstrong number");
    else:
        print(f"{y} is not an armstrong number");
q=input("enter a number to check armstrong possibility\n");
arm(q);
    
#9 tables
for i in range(1,11):
    print(f"9*{i}={9*i}");

#positive/negative
def po(n):
    if(n>=0):
        print("positive");
    else:
        print("negative");
n=int(input("enter a number to check whether it is positive or negative"))
po(n);

#days to ages
n=int(input("enter the days:"))
print(f"age={n//365}");

#tringnometry
import math
s=math.sin(90)*2+math.cos(90)*2
print(f"(sin90)^2+(cos90)^2={s}")

#Simple calculator
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Select the operator:*,+,-,/")
if c=='*':print(f"{a}*{b}={a*b}")
elif c=='/':print(f"{a}/{b}={a/b}")
elif c=='+':print(f"{a}+{b}={a+b}")
elif c=='-':print(f"{a}-{b}={a-b}")
      
    
    
