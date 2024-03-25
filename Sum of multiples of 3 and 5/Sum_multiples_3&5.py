#Find the sum of multiples of 3 & 5

def multiples(list1):
    sum=0
    for i in list1:
        if(i%3==0) or (i%5==0):
            sum+=i
            print(i)
    return sum
list1=[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("List",list1)
print("Sum of multiples of 3 & 5 is",multiples(list1))


