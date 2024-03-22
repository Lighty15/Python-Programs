#To print star series

def star_pattern(rows):
    for i in range(1,rows+1):
        for j in range(i):
            print('*',end='')
        print()
        
n=5
star_pattern(n)
