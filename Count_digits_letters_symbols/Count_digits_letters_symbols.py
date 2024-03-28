#Count all digits, letters and special symbols in a string

def count(str1):
    digit=0
    letter=0
    symbol=0
    for i in str1:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letter+=1
        else:
            symbol+=1
    print("Digits count:",digit)
    print("Letters count:",letter)
    print("Special symbols count:",symbol)
str1=input("Enter a string:")
count(str1)
