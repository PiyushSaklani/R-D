# Initial Code without any threads

import numpy as np
from datetime import datetime
import time

start = time.time()
now = datetime.now()
start_time = now.strftime("%H:%M:%S")

zero_matrix = np.zeros((100,100))

print("Random value allocation Starts...")
for i in range(len(zero_matrix)):
    for j in range(len(zero_matrix)):
        zero_matrix[i][j] = np.random.choice([0,1,2,3,4,5,6,7])

print("Process Completed")

end = time.time()
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print(f"\n\tStarted at : {start_time}\n\tEnd at : {end_time}\n\n\tTime taken : {(end-start)} s")