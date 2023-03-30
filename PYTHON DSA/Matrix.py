import numpy as np

a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])
m = np.reshape(a,(4, 4))
print(m)

print("\nAccessing Elements")
print(a[1])
print(a[2])

m = np.append(m,[[1,22,33,55]],0)
print("\nAdding")
print(m)