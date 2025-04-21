import numpy as np

# Код оголошення векторів не можна змінювати
a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])

# 1. Sum of a and b
sum_ab = a + b
print(f"Sum of a and b:\n{sum_ab}")

# 2. Difference of a and b
diff_ab = a - b
print(f"\nDifference of a and b:\n{diff_ab}")

# 3. Sum of a and b^T
b_transpose = b.T
try:
    sum_ab_transpose = a + b_transpose
    print(f"\nSum of a and b^T:\n{sum_ab_transpose}")
except ValueError as e:
    print(f"\nError during sum of a and b^T: {e}")
    print("Explanation: The sum of a and b^T cannot be calculated because the shapes are incompatible. 'a' has shape (1, 5) and 'b^T' has shape (5, 1). NumPy requires compatible shapes for element-wise operations.")

# 4. Matrix product (dot product) of a and b^T
dot_ab_transpose = np.dot(a, b_transpose)
print(f"\nDot product of a and b^T:\n{dot_ab_transpose}")

# 5. Matrix product (dot product) of a and b
try:
    dot_ab = np.dot(a, b)
    print(f"\nDot product of a and b:\n{dot_ab}")
except ValueError as e:
    print(f"\nError during dot product of a and b: {e}")
    print("Explanation: The dot product of a and b cannot be calculated because the shapes are incompatible. 'a' has shape (1, 5) and 'b' has shape (1, 5). For matrix multiplication, the number of columns in the first matrix must match the number of rows in the second matrix.")

# 6. Hadamard product of a and b
hadamard_ab = np.multiply(a, b)
print(f"\nHadamard product of a and b:\n{hadamard_ab}")
print("Explanation: The Hadamard product is an element-wise multiplication. Each element in 'a' is multiplied by the corresponding element in 'b'.")

# 7. Division of a by b
division_ab = np.divide(a, b)
print(f"\nDivision of a by b:\n{division_ab}")
print("Explanation: The division is performed element-wise. Each element in 'a' is divided by the corresponding element in 'b'.")

# 8. Division of a by b^T
try:
    division_ab_transpose = np.divide(a, b_transpose)
    print(f"\nDivision of a by b^T:\n{division_ab_transpose}")
except ValueError as e:
    print(f"\nError during division of a by b^T: {e}")
    print("Explanation: The division of a by b^T cannot be calculated because the shapes are incompatible. 'a' has shape (1, 5) and 'b^T' has shape (5, 1). NumPy requires compatible shapes for element-wise operations.")
