import numpy as np
import easynn as nn

# Create a numpy array of 10 rows and 5 columns.
# Set the element at row i and column j to be i+j.
def Q1():
    a = np.empty([10,5])
    for i in range(10):
        for j in range(5):
            a[i,j] = i+j

    return a

# Add two numpy arrays together.
def Q2(a, b):
    return a+b

# Multiply two 2D numpy arrays using matrix multiplication.
def Q3(a, b):
    return a @ b

# For each row of a 2D numpy array, find the column index
# with the maximum element. Return all these column indices.
def Q4(a):
    indices = []
    for r in a:
        indices.append(np.argmax(r))
    return indices

# Solve Ax = b.
def Q5(A, b):
    return np.linalg.solve(A,b)

# Return an EasyNN expression for a+b.
def Q6():
    a = nn.Input("a")
    b = nn.Input("b")
    return a+b

# Return an EasyNN expression for a+b*c.
def Q7():
    a = nn.Input("a")
    b = nn.Input("b")
    c = nn.Input("c")
    return a+b*c

# Given A and b, return an EasyNN expression for Ax+b.
def Q8(A, b):
    A = nn.Const(A)
    b = nn.Const(b)
    x = nn.Input("x")
    return A*x + b

# Given n, return an EasyNN expression for x**n.
def Q9(n):
    x = nn.Input("x")
    m = x
    for i in range(1,n):
        m = m*x

    return m
    
# Return an EasyNN expression to compute
# the element-wise absolute value |x|.
def Q10():
    x = nn.Input("x")
    relu = nn.ReLU()
 
    return relu(x) + relu(-x)