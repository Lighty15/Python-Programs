#Print the index of a character in a string

def index_char(str):
    
    for index,char in enumerate(str):
        print(char,"position at",index)

str=input("Enter a string:")
index_char(str)
