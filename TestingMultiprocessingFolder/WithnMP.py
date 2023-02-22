import multiprocessing as mp
import numpy as np
from datetime import datetime
import time


def inmatrix(zero_matrix,n,m):
    for i in range(n):
        for j in range(m):
            zero_matrix[i][j] = np.random.choice([0,1,2,3])
    # time.sleep(5)


if __name__ == "__main__":
    start = time.time()
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    n,m = 1,100
    matrix = np.zeros((n,m))


    mprocess = list()
    for index in range(100):
        x = mp.Process(target=inmatrix,args=(matrix,n,m,))
        mprocess.append(x)
        x.start()

    # print(mprocess)

    for index,process in enumerate(mprocess):
        process.join()

    # print(f"\033[33mThreads : {threads}\033[00m") 

    print(mprocess)

    end = time.time()
    now = datetime.now()
    end_time = now.strftime("%H:%M:%S")
    print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s")