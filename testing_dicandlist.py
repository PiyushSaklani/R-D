import numpy as np
from datetime import datetime
import time

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")

zero_matrix = np.zeros((10000,10000))
# f = open("myfile.txt", "w")
# f = open("myfile.txt", "x")

print(1)
for i in range(len(zero_matrix)):
    for j in range(len(zero_matrix)):
        zero_matrix[i][j] = np.random.choice([0,1,2,3,4,5,6,7])

print(2)
# f = open("myfile.txt", "a")
# for i in zero_matrix:
#     for j in i:
#         f.write(f"{str(int(j))} ")
#     f.write("\n")
# f.close()

# print(zero_matrix)

end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\tStarted at : {start_time}\n\tEnd at : {end_time}\n\n\tTime taken : {(end-start) * 10**3} ms")