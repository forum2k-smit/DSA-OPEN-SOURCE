# Creating a function for the linear search algorithm
def linearSearch(array, numbersInArray, x):
    # Looping in range of 0 to the total number of items input by the user
    for i in range(0, numbersInArray):
        if (array[i] == x):  # If x is present then returning its index
            return i
    else:
        return -1  # else we will return -1


arrayToBeSearched = []  # We will create an empty list where we can append the input
# Asking for the number of items we want in the array
numbersInArray = int(input("How many numbers do you want your array to have?"))

# Looping in range of 0 to the total number of items input by the user
for items in range(0, numbersInArray):
    addNum = int(input("Enter a number:"))  # take a user input
    # append the user input to the empty array and continue the loop till the range
    arrayToBeSearched.append(addNum)

# we take input for the desired number to be searched
x = int(input("Enter the desired element you want to find:"))

# Creating an instance of the function with the user inputs
result = linearSearch(arrayToBeSearched, numbersInArray, x)

if(result == -1):
    # if the function returns -1 we print that the element was not found
    print("Element not found")
else:
    # else we print the index of the element
    print("Element found at index: ", result)
