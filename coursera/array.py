import numpy as np

X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)

print(Z)


################3


X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
print(out)