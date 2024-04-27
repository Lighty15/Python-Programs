#Python program to swap elements in a list

def swap(list,position1,position2):
    list[position1],list[position2]=list[position2],list[position1]
    print("After swapping",list)

list=[2,4,6,8]
position1,position2=1,3
print("Before swapping",list)
swap(list,position1-1,position2-1)

