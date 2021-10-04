# Done By :: Vivaan Shiromani 
# Date :: 4th Oct 2021

# Program to implement Bubble Sort Alogorithm in Python.
# Time Complexity :: O(n^2)

lst=[4,5,-1,-3,5,9,10,11,99]
# Output: [-3, -1, 4, 5, 5, 9, 10, 11, 99]
# lst=[3,2]
# Output: [2,3]

# Steps: 
# 1. Bubble sort means to compare the ith and i+1th element ; if ith one is greater than 
#    i+1th then they will swap, if not then no change will happen.

# 2. In this algorithm we considered a variable dec which is initialized to 1, why ? because
#    in the for loop we are comparing with i and i+1th values if we initialize to 0, it will
#    go out of range.

# 3. The inner for is for comparing the values and outer while loop is for checking that, if
#    dec will become len(lst)-1 it will stop as we cannot decrement more.

# 4. The sorted values will be modified in the same list.
 
dec=1
while(dec != len(lst)-1):
    for i in range(0, len(lst)-dec):
        if(lst[i] > lst[i+1]):
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
        else:
            continue
    dec+=1
print(lst)