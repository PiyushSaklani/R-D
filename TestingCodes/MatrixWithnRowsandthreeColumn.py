import numpy as np 
#* pip install numpy or pip3 install numpy
from datetime import datetime
import time

#! Functions
def filter_list(check_list,a,b):
    return len(list(filter(lambda x: a <= x <= b, check_list)))

def check_pct(check_list,range_list):
    for a,b in range_list:
        print(f"\033[90mPercentage of numbers in the range {a}-{b} : {round(filter_list(check_list,a,b) / len(check_list) * 100,2)}\033[00m")

def random_valandpct(range_list,population_pct,all_lists,p):
    for i,j in zip(range_list,population_pct):
        temp_list = list(range(i[0],i[1]))
        all_lists = all_lists + temp_list
        p = p + [j/len(temp_list)]*len(temp_list)
    return all_lists,p

#* Comment 1: Time function which returns the current time.
def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


#! Code
#* Comment 2: Noting the code start time 
start_time = current_time()
start = time.time()

#* Comment 3: Defining the number of rows in the matrix.
rows = 100

#* Age Group = 0-4, 5-19, 20-24, 25-60, 60+
#* Comment 4: This is a interaction range according to the age group.
range_list = [[100,125],[150,175],[200,250],[300,325],[350,375]]

#* Comment 5: This is a population percentage according to the age group.
population_pct = [0.08,0.28,0.1,0.45,0.09]

#* Comment 6: List which stores the values and percentage for random selection.
all_lists, p = random_valandpct(range_list,population_pct,[],[])

#* Comment 7: Create a list of random integer values.
int_list = np.random.choice(all_lists, size=rows, p=p)

#* Comment 8: Create an empty matrix.
matrix = np.empty((rows, 3), dtype=object)

#* Comment 9: Assigning empty list in the 0 and 1 index.
for i in range(rows):
    matrix[i, 0] = []
    matrix[i, 1] = []

#* Comment 10: Assigning random value to the 2 index which are stored in the "int_list".
matrix[:, 2] = np.random.choice(int_list, size=rows)

#* Comment 11: Saving the whole matrix in the matrix.txt file.
np.savetxt("matrix.txt", matrix, delimiter=",", fmt='%s')

#* Comment 12: Noting the code ending time.
end = time.time()
end_time = current_time()

#* Comment 13: Printing the Code Runtime.
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")

#* Comment 14: Checking that random values are in correct propotion.
# check_pct(int_list,range_list)