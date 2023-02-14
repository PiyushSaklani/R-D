import numpy as np
from datetime import datetime
import time
import threading

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")
# global test, a, b
# a,b = 1,1000
matrix = np.zeros((1,10000))
# test = np.zeros((a,b))

def inmatrix(zero_matrix):
    # global test
    for i in range(1):
        for j in range(10000):
            zero_matrix[i][j] = np.random.choice([0,1,2,3])
    # test = np.concatenate((test,zero_matrix),axis=0)

threads = list()
for index in range(10000):
    x = threading.Thread(target=inmatrix, args=(matrix,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()

# print(f"\033[33mThreads : {threads}\033[00m")
# print(test)

end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start) * 10**3} ms")