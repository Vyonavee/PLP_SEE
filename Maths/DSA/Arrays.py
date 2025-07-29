#Index : 0 1 2 3 4 5
#array   5 10 15 20 25
arr=[10,20,30,40,50]

#print(arr[2])
arr[2]=55

#print(arr[2])

#inserting at the end (append)
arr.append(60)
print(arr)
#insert at a position
arr.insert(2,25)
print(arr)

#delete (pop) an array
arr.pop(3)
print(arr)

#search a value
if 50 in arr:
    print("Found 50")