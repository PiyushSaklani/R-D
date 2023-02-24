import threading
import random
import time
from tqdm import tqdm

start = time.time()

n_rows = 1000000
n_cols = 3

# Define the number of threads to use
n_threads = 10000

# Define a lock to synchronize access to the matrix
matrix_lock = threading.Lock()

# Define a function to generate random values for a subset of the rows
def fill_rows(start, end):
    global matrix
    for i in range(start, end):
        matrix_lock.acquire()
        matrix[i][0] = []
        matrix[i][1] = []
        matrix[i][2] = random.randint(1, 100)
        matrix_lock.release()

# Create the empty matrix
matrix = [[[], [], 0] for i in range(n_rows)]

# Create the threads and start them
threads = []
for i in tqdm(range(n_threads)):
    start = (n_rows // n_threads) * i
    end = (n_rows // n_threads) * (i + 1)
    t = threading.Thread(target=fill_rows, args=(start, end))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

end = time.time()
print(f"\033[36m\033[01mTime taken : {(end-start)} s")
