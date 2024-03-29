#Count number of vowels, consonants and white spaces in a string

string=input("Enter a string:")
vowels=consonants=white_space=0
for i in string:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowels+=1
        else:
            consonants+=1
    else:
        white_space+=1
        
print("Number of vowels:",vowels)
print("Number of consonants:",consonants)
print("Number of white spaces:",white_space)
