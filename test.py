# import numpy as np
# from datetime import datetime
# import time
# import threading

# start = time.time()
# now = datetime.now()
# start_time = now.strftime("%H:%M:%S")

# a = np.zeros((100,1000))
# b = np.zeros((100,1000))
# c = np.zeros((100,1000))
# d = np.zeros((100,1000))
# e = np.zeros((100,1000))
# f = np.zeros((100,1000))
# g = np.zeros((100,1000))
# h = np.zeros((100,1000))
# i = np.zeros((100,1000))
# j = np.zeros((100,1000))

# global test
# test = []
# def inmatrix(zero_matrix):
#     for i in range(100):
#         for j in range(1000):
#             zero_matrix[i][j] = np.random.choice([0,1,2,3])

#     test.append(zero_matrix)


# t1 = threading.Thread(target=inmatrix,args=(a,))
# t2 = threading.Thread(target=inmatrix,args=(b,))
# t3 = threading.Thread(target=inmatrix,args=(c,))
# t4 = threading.Thread(target=inmatrix,args=(d,))
# t5 = threading.Thread(target=inmatrix,args=(e,))
# t6 = threading.Thread(target=inmatrix,args=(f,))
# t7 = threading.Thread(target=inmatrix,args=(g,))
# t8 = threading.Thread(target=inmatrix,args=(h,))
# t9 = threading.Thread(target=inmatrix,args=(i,))
# t10 = threading.Thread(target=inmatrix,args=(j,))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()

# print(test)

# end = time.time()
# now = datetime.now()
# end_time = now.strftime("%H:%M:%S")
# print(f"\n\tStarted at : {start_time}\n\tEnd at : {end_time}\n\n\tTime taken : {(end-start) * 10**3} ms")

a = [1,2,3,4,5]
b = [7,6,5]

print(b in a)
z = b[1:]
print(b[1:] in a)
print(all(x in a for x in b[1:]))