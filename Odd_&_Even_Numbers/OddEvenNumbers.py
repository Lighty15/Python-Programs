#PRINT ALL ODD NUMBERS AND EVEN NUMBERS UPTO n

def oddeven(n):
    
    print("Even numbers upto",n,":")
    for i in range(0,n+1):
        if i%2==0:
            print(i)

    print("Odd numbers upto",n,":")
    for i in range(0,n+1):
        if i%2!=0:
            print(i)

n=10
oddeven(n)
