#Sorting the words in alphabetic order

def sort_words(str):

    words=[word.lower() for word in str.split()]
    words.sort()

    print("The sorted words are:")
    
    for word in words:
        print(word)

str=input("Enter the string:")
sort_words(str)
