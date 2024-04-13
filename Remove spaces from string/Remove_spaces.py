#Remove spaces from a string

def remove_space(str):
    str=str.replace(' ', '')
    return str

str=input("Enter a string:")
print(remove_space(str))
