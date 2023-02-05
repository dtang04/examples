import numpy as np
matrix = np.array([[[1,2,3,4],[4,5,6,7]], [[10,20,30,40],[40,50,60,70]]])
print(matrix.ndim) #ndim returns how many dimensions there are to a matrix
print(matrix.shape) #2 elements in outermost list, 2 elements in middle, 4 elements in innermost list
print(matrix.size) #prints how many elements there are
print(np.zeros((2,10))) #prints a 2 by 10 matrix of zeros
print(np.ones((3,2,5))) #prints a 3 by 2 by 5 matrix of ones
print(np.arange(1,10,0.5)) #iterates by step (0.5) from [1,10), returns a numpy array containing values
print(np.arange(10))
print(np.linspace(0,100,7)) #divides a space [0,100] into seven parts
#data = np.loadtxt("file-name", delimiter = ",") loads a file into a numpy array by delimiter
"""
Matrix indexing and slicing
"""
value = matrix[0][1][3] #value is now 7
value = matrix[0,1,3] #same indexing
print(value)
lst = matrix[0] #list of lists
print(lst, type(lst))
b = np.array([[0, 1, 4, 9],
              [16, 25, 36, 49],
              [64, 81, 100, 121],
              [144, 169, 196, 225],
              [256, 289, 324, 361],
              [400, 441, 484, 620]])
sub = b[0:3,1:3] #get rows from [0,3), and then in each row get columns from [1,3)
print(sub)
b[:,2] = np.arange(6) #we can also use slicing to update the original object
print(b)
def compute_col_mean(data,j):
    numterms = data.shape[0]
    return sum(data[:,j])/numterms
print(compute_col_mean(b,3))
"""
Array Operations
"""
a = np.arange(7)
print(a)
a = a * 2 #element wise multiplication (not [0,1,2,3,4,5,6,0,1,2,3,4,5,6])
print(a)
a2d = np.array([[1,2,3,4],[5,6,7,8]])
print("a2d:\n", a2d)
a2dmult = a2d * 2 #element wise multiplication
print("a2d*2:\n", a2dmult)
a2dadd = a2d + 2
print("a2d+2:\n", a2dadd)
a2dgreater2 = a2d > 2
print("a2d>2:\n", a2dgreater2)
a2dequal2 = a2d == 2
print("a2d==2:\n", a2dequal2)
def compute_column_stdev(data,j):
    col = data[:,j]
    numterms = data.shape[0]
    colmean = sum(col)/numterms
    return (sum((col - colmean)**2)/numterms) ** (1/2)
print(compute_column_stdev(b,3))
b2d = np.array([[4,5,6,7],[10,12,15,18]])
matrixsum = a2d + b2d #numPy also allows summing matrices of same dimensions
print(matrixsum)
elemult = a2d * b2d #element-wise multiplication
print(elemult)
b2d = np.array([[1,2],[3,4],[5,6],[7,8]])
matrixmult = np.dot(a2d,b2d) #matrix-matrix multiplication
print(matrixmult)
"""
Reshaping numPy arrays
"""
a = np.arange(12)
print(a)
a = a.reshape(3,4) #reshapes a into matrix with three rows, four columns
print(a)
try:
    print("Does a.reshape(3,5) work?")
    a.reshape(3,5)
except Exception:
    print("No, as the number of entries in reshaped matrix don't match the number of entries in the old matrix.")
b = np.arange(10)
c = b.reshape(2,5)
c[1,4] = 99
print("c:\n", c, "\nb:\n", b) #notice that reshape doesn't create a new copy of the original array; when we update one array, it updates the other array.
"""
Means and Standard Deviation
"""
b = (np.arange(24) ** 2).reshape(6, 4)
print(b)
colmeans = np.array([np.mean(b[:,0]),np.mean(b[:,1]),np.mean(b[:,2]),np.mean(b[:,3])])
print("Column means calculated column by column: ", colmeans)
colmeans = np.mean(b, axis = 0) #Notice that axis = 0 is operations on each column, contrary to row x col conventions
print("Column means using 'axis' parameter (axis = 0): ", colmeans)
rowmeans = np.mean(b, axis = 1)
print("Row means using 'axis parameter (axis = 1: ", rowmeans)
print("Column standard deviations: ", b.std(axis = 0))
print("Row standard deviations: ", b.std(axis = 1))
"""
Fancy Indexing
"""
a = np.arange(100,112)
print("a =", a)
print("We can specify multiple index positions with a list of indices: \na[[1,2,3,4]] =", a[[1,2,3,4]])
print("If we specify a multidimensional array, then numPy will return the indices in the spcified order:")
print("a[[[1,2],[3,4]]] =\n", a[[[1,2],[3,4]]])
print("Indexing with booleans produces a 1-D array with only 'True' values being indexed:")
c = np.arange(5)
print("c[np.array([True,True,False,True,False])] =", c[np.array([True,True,False,True,False])]) #have to use np.array
b = (np.arange(24) ** 2).reshape(6, 4)
print("b =\n", b)
print("Get a boolean matrix corresponding with b > 100: \n", b > 100)
print("Then get only True values of that boolean matrix (b[b > 100]): \n", b[b>100])
"""
Filtering
"""
b[(b > 100) & (b % 2 == 0)] = 0 #Since bitwise operators have higher precedence than relational operators, use parenthesis
print("b[(b > 100) & (b % 2 == 0)] = 0 \n b =\n", b)
b = (np.arange(24) ** 2).reshape(6, 4)
b[(b > 100) | (b % 2 > 1)] = 3
print("b[(b > 100) | (b % 2 > 1)] = 3 \n b =\n", b)
