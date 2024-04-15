#Find length of the longest word in a list

def longest_word(list):
    word_length=[]

    for n in list:
        word_length.append((len(n),n))

    word_length.sort()
    return word_length[-1][0],word_length[-1][1]

Result=longest_word(["Hi", "Friends"])
print("\nLongest word:",Result[1])
print("Length of the longest word:",Result[0])
