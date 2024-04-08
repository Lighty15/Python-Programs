#Calculate Simple interest

def simple_interest(p,t,r):
    SI=(p*t*r)/100
    print("Simple Interest:",SI)
    
p=int(input("Enter the principal amount:"))
t=int(input("Enter the time period:"))
r=int(input("Enter the rate of interest:"))
simple_interest(p,t,r)
