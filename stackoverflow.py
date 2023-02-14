import numpy as np
import threading

row,column = 1,1000
matrix = np.zeros((row,column))

def inmatrix(matrix):
    global row,column
    for i in range(row):
        for j in range(column):
            matrix[i][j] = np.random.choice([0,1,2,3])

threads = list()
for index in range(1000):
    x = threading.Thread(target=inmatrix, args=(matrix,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()