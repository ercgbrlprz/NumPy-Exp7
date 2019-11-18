import numpy as np
X = np.random.random((5,5))
xBar = np.mean(X)
sDev = np.std(X)
Z = (X-xBar)/sDev