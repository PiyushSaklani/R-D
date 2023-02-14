# Code with n threads

import numpy as np
from datetime import datetime
import time
import threading

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")
n,m = 1,100
matrix = np.zeros((n,m))
print(matrix)

def inmatrix(zero_matrix):
    global n,m
    for i in range(n):
        for j in range(m):
            zero_matrix[i][j] = np.random.choice([0,1,2,3])
    # time.sleep(5)

threads = list()
for index in range(100):
    x = threading.Thread(target=inmatrix, args=(matrix,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()

# print(f"\033[33mThreads : {threads}\033[00m")

end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s")