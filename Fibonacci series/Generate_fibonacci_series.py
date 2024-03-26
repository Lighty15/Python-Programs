#Python program to generate fibonacci series upto N terms

def fibonacci_series(N):
    a=0
    b=1
    c=a+b
    print("Fibonacci series upto",N,"terms:")
    if N==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(3,N+1):
            print(c)
            a=b
            b=c
            c=a+b
            
N=int(input("Enter no of terms:"))
fibonacci_series(N)
