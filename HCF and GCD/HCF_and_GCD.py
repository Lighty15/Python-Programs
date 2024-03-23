#Compute HCF and GCD of two numbers using function

def find_GCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0) and (y%i==0):
            gcd=i
    return gcd

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print("GCD of",num1,"and",num2,"is",find_GCD(num1,num2))

