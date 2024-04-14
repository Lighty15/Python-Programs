#Remove duplicates from a string

def remove_duplicate(str):
    
    a=set(str)
    a="".join(a)
    b=""

    print("\nWithout duplicates")
    
    for i in str:
        if (i in b):
            pass
        else:
            b=b+i
        print(b)

str=input("Enter a string:")
remove_duplicate(str)
