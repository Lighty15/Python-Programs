#Python program to find the factors of a given number

def factors(n):
    print("The factors of",n,"are")
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            
num1=int(input("Enter a number:"))
factors(num1)
