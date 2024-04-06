#Count the vowels in a string

def count_vowels(str1):

    count=0
    
    for i in str1:
        if i.isalpha():
            if i.lower() in 'aeiou':
                count+=1
    print("Vowers count:",count)

str1=input("Enter a string:")
count_vowels(str1)
