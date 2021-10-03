def linearSearch(array, numbersInArray, x):
    for i in range(0, numbersInArray):
        if (array[i] == x):
            return i
    else:
        return -1

myArray = []
numbersInArray = int(input("How many numbers do you want your array to have?"))

for items in range(0, numbersInArray):
    addNum = int(input("Enter a number:"))
    myArray.append(addNum)

x = int(input("Enter the desired element you want to find:"))

result = linearSearch(myArray, numbersInArray, x)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

