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

#! Code
#* Comment 1: Time function which returns the current time.
def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

#* Comment 2: Noting the code start time 
start_time = current_time()
start = time.time()

#* Comment 3: Defining the number of rows in the matrix.
rows = 100

#* Comment 4: This is a interaction range according to the age group.
range_list = [[1,10]]

#* Comment 5: This is a population percentage according to the age group.
population_pct = [1]

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

#! Writing new code

connections = list(range(0,rows-1))
print(f"{connections=}")
loopsize = matrix[0,2]-len(matrix[0,0])
print(f"{len(connections)=} , {len(list([1/rows]*(rows-1)))=}")
interaction = np.random.randint(connections,size=loopsize)
print(f"{interaction=}")
i = 0
while i < len(matrix):
    loopsize = matrix[i,2]-len(matrix[i,0])
    interaction = np.random.choice(connections,size=loopsize)
    weight = np.random.choice([1,2,3],size=loopsize)
    for j in range(loopsize):
        matrix[i,0].append(interaction[j])
        matrix[i,1].append(weight[j])
        matrix[interaction[j],0].append(i)
        matrix[interaction[j],1].append(weight[j])
    i += 1

#! -- -- -- -- -- --

#* Comment 11: Saving the whole matrix in the matrix.txt file.
np.savetxt("test_matrix.txt", matrix, delimiter=",", fmt='%s')

#* Comment 12: Noting the code ending time.
end = time.time()
end_time = current_time()

#* Comment 13: Printing the Code Runtime.
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")

#* Comment 14: Checking that random values are in correct propotion.
# check_pct(int_list,range_list)