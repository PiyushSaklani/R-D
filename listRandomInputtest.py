import numpy as np 
#* pip install numpy or pip3 install numpy
import random as rm
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
rows = 50

#* Comment 4: This is a interaction range according to the age group.
range_list = [[1,2],[5,8],[10,15]]

#* Comment 5: This is a population percentage according to the age group.
population_pct = [0.33,0.33,0.34]

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

interaction_level = [1,2,3]
print(f"{interaction_level=}")

population_alc_list = list(range(0,rows))
print(f"{population_alc_list=}")

# population_alc_pct = [1/rows]*rows
# print(f"{population_alc_pct=}")

sumofallInteraction = 0
for j in range(rows): sumofallInteraction += matrix[j, 2]
print(f"\033[33m{sumofallInteraction=}")

for k in range(rows):
    # print(f"\n{k=} {matrix[k, 2]=}")
    l = 1
    while len(matrix[k, 0]) < matrix[k, 2]:

        relation = rm.choice(population_alc_list)
        interaction = rm.choice(interaction_level)

        # print(f"{relation=} {l=}")
        # time.sleep(0.5)

        if relation not in matrix[k, 0] and k not in matrix[relation, 0] and k != relation:
            matrix[k, 0].append(relation)
            matrix[k, 1].append(interaction)
            matrix[relation, 0].append(k)
            matrix[relation, 1].append(interaction)

        elif all(x in matrix[k, 0] for x in population_alc_list[1:]):
            # print(f"{population_alc_list[1:]=}")

            new_row = np.array([[[], [], 0]], dtype=object)
            matrix = np.append(matrix, new_row, axis=0)

            population_alc_list.append(len(matrix)-1)

            matrix[k, 0].append(len(matrix)-1)
            matrix[k, 1].append(interaction)
            matrix[len(matrix)-1, 0].append(k)
            matrix[len(matrix)-1, 1].append(interaction)

        np.savetxt("test_matrix.txt", matrix, delimiter=",", fmt='%s')
        l += 1

    population_alc_list.remove(k)
    # print(f"{population_alc_list=}")
    

sumofallFINALInteraction = 0
for j in range(rows): sumofallFINALInteraction += len(matrix[j, 0])
print(f"{sumofallFINALInteraction=}\033[00m")
print(f"\033[92m{sumofallFINALInteraction-sumofallInteraction}\033[00m")

#! -- -- -- -- -- --

#* Comment 11: Saving the whole matrix in the matrix.txt file.
np.savetxt("test_matrix.txt", matrix, delimiter=",", fmt='%s')

#* Comment 12: Noting the code ending time.
end = time.time()
end_time = current_time()

#* Comment 13: Printing the Code Runtime.
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")

#* Comment 14: Checking that random values are in correct propotion.
check_pct(int_list,range_list)
