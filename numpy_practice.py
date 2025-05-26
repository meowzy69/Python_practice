import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])


# Special Arrays
zeros = np.zeros(3)        
ones = np.ones((2, 2))       
range_arr = np.arange(0, 10, 2)  
random_arr = np.random.rand(3)   

print("\nZeros:", zeros)
print("Ones:\n", ones)
print("Range Array:", range_arr)
print("Random Array:", random_arr)

# Calculations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum = a + b
diff = a - b
prod = a * b
div = a / b

print(sum)
print(diff)
print(prod)
print(div)

# Reshape, shape, and slicing

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[:, 1])  # Second column
print(matrix[1, :])  # Second row
print(matrix[0, 1])  # Element at first row, second column

# Statistical functions

a = np.array([2, 4, 6, 8, 10])

print(np.mean(a))  # Mean
print(np.median(a))  # Median
print(np.std(a))  # Standard Deviation

# Practice problems

a = np.array([1, 2, 3, 4, 5])
total = np.sum(a)
print("Total:", total)

# filter even numbers

number = np.array([1, 2, 3, 4, 5, 6])
even_numbers = number[number % 2 == 0]
print("Even Numbers:", even_numbers)

f = [False, True, '2', 3.0]
print(type(f)) 

#Random ques

z = np.array([[1, 1, 1], [3, 4, 4]])
print(z[1:, :1])

