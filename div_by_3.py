import numpy as np
C = np.arange(1,101)
B = np.reshape(C, (10,10))
A = np.square(B)
divBy3 = A[A%3 == 0]