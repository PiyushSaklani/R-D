# Code with 10 threads

import numpy as np
from datetime import datetime
import time
import threading

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")

n,m = 10,100

a = np.zeros((n,m))
b = np.zeros((n,m))
c = np.zeros((n,m))
d = np.zeros((n,m))
e = np.zeros((n,m))
f = np.zeros((n,m))
g = np.zeros((n,m))
h = np.zeros((n,m))
i = np.zeros((n,m))
j = np.zeros((n,m))

global test
test = []
def inmatrix(zero_matrix):
    global n,m
#   zero_matrix = np.zeros((250,250))
    for i in range(n):
        for j in range(m):
            zero_matrix[i][j] = np.random.choice([0,1,2,3])

    test.append(zero_matrix)
    return zero_matrix

t1 = threading.Thread(target=inmatrix,args=(a,))
t2 = threading.Thread(target=inmatrix,args=(b,))
t3 = threading.Thread(target=inmatrix,args=(c,))
t4 = threading.Thread(target=inmatrix,args=(d,))
t5 = threading.Thread(target=inmatrix,args=(e,))
t6 = threading.Thread(target=inmatrix,args=(f,))
t7 = threading.Thread(target=inmatrix,args=(g,))
t8 = threading.Thread(target=inmatrix,args=(h,))
t9 = threading.Thread(target=inmatrix,args=(i,))
t10 = threading.Thread(target=inmatrix,args=(j,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

# print(test)

print("Done For 100X100")

end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\tStarted at : {start_time}\n\tEnd at : {end_time}\n\n\tTime taken : {(end-start)} s")