list=[2,3,4,6,8]
print("List:",list)

search=int(input("Enter the element to search:"))

for i in range(len(list)):
    if(search==list[i]):
        print("The element is present in",i)
        break
else:
    print("The element is not present")
