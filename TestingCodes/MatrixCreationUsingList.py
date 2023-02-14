import numpy as np
from datetime import datetime
import time

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")

# Create a list of values from which to generate random values
value_list = [1, 2, 3, 4, 5]

# Create a 1000x1000 matrix with random values in integers from the value_list
matrix = np.random.choice(value_list, size=(10000, 10000))

# Saving the matrix in a .txt file
np.savetxt("matrix.txt", matrix, delimiter=",", fmt='%d')


end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s")