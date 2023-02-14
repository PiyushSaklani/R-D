import numpy as np
from datetime import datetime
import time
import threading

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")
f = open("mymatrix.txt", "w")
# f = open("mymatrix.txt", "x")

global test, a, b
a,b = 1,1000
matrix = np.zeros((a,b))
test = np.zeros((a,b))

def inmatrix(zero_matrix):
    global test
    for i in range(a):
        for j in range(b):
            zero_matrix[i][j] = np.random.choice([0,1,2,3])
    test = np.concatenate((test,zero_matrix),axis=0)

threads = list()
for index in range(1000):
    x = threading.Thread(target=inmatrix, args=(matrix,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()

# print(f"\033[33mThreads : {threads}\033[00m")
print(test)

print(2)
f = open("mymatrix.txt", "a")
for i in test:
    for j in i:
        f.write(f"{str(int(j))} ")
    f.write("\n")
f.close()


end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start) * 10**3} ms")