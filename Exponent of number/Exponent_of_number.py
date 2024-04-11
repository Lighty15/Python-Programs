#Exponent of a number

def power(base,exponent):
    
    if (exponent==1):
        return base
    else:
        return base*power(base,exponent-1)

base=int(input("Enter base:"))
exponent=int(input("Enter exponential value:"))
print(power(base,exponent))
