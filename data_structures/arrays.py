numbers = [1,2,3,4,5,6,10,3]

# adding an element at the end: O(1)
numbers.append(1);
print(numbers)

# Adding an element at some index: O(n) because all elements after this index will be shifted
numbers[1] = '90'

# Find the max of the array is of O(N)
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)