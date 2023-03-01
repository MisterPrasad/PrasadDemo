a=int(input('Enter first number'))
b=int(input('Enter second number'))
i=1
while(a>i and b>i):
    if(a%i==0 and b%i==0):
        n=i
    i+=1
print(n)