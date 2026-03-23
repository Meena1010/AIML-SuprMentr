import time
import numpy as np

size = 1000000

start = time.time()
py_list = [i * 2 for i in range(size)]
end = time.time()
print("Python list time:", end - start)

start = time.time()
np_array = np.arange(size) * 2
end = time.time()
print("NumPy array time:", end - start)