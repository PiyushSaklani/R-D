import numpy as np 
#* pip install numpy or pip3 install numpy
import random as rm
#* pip install random
from tqdm import tqdm
#* pip install tqdm
from datetime import datetime
import time

#! Functions
def filter_list(check_list,a,b):
    return len(list(filter(lambda x: a <= x <= b, check_list)))

def check_pct(check_list,range_list):
    acc = 0
    for a,b in range_list:
        val = round(filter_list(check_list,a,b) / len(check_list) * 100,2)
        print(f"\033[90mPercentage of numbers in the range {a}-{b} : {val}\033[00m")
        acc += val
    
    return acc

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

def append_matrix(x,y,z):
    global matrix
    matrix[x, 0].append(y)
    matrix[x, 1].append(z)
    matrix[y, 0].append(x)
    matrix[y, 1].append(z)

print("\n\t\033[01m\033[34mStarted\n\033[00m")

#! Code
#* Comment 2: Noting the code start time 
start_time = current_time()
start = time.time()

#* Comment 3: Defining the number of rows in the matrix.
rows = 100000

#* Age Group = 0-4, 5-19, 20-24, 25-60, 60+
#* Comment 4: This is a interaction range according to the age group.
range_list = [[100,125],[150,175],[200,250],[300,325],[350,375]]

#* Comment 5: This is a population percentage according to the age group.
population_pct = [0.08,0.28,0.1,0.45,0.09]

#* Comment 6: This is a interaction level.
interaction_level = [1,2,3]

#* Comment 7: List which stores the values and percentage for random selection.
all_lists, p = random_valandpct(range_list,population_pct,[],[])

#* Comment 8: Create a list of random integer values.
int_list = np.random.choice(all_lists, size=rows, p=p)

#* Comment 9: Create an empty matrix.
matrix = np.empty((rows, 3), dtype=object)

#* Comment 10: Assigning empty list in the 0 and 1 index.
for i in tqdm(range(rows)):
    matrix[i, 0] = []
    matrix[i, 1] = []

#* Comment 11: Assigning random value to the 2 index which are stored in the "int_list".
matrix[:, 2] = np.random.choice(int_list, size=rows)

#* Comment 12: This is a list of population.
population_alc_list = list(range(0,rows))

print()

for k in tqdm(range(rows)):
    while len(matrix[k, 0]) < matrix[k, 2]:

        #* Comment 13: This is a interaction and interaction level.
        relation = rm.choice(population_alc_list)
        interaction = rm.choice(interaction_level)

        #* Comment 14: Checking that they did not have relation before and person did not get interaction with them self.
        if relation not in matrix[k, 0] and k not in matrix[relation, 0] and k != relation:
            #* Comment 15: Appending interaction and interation value in the matrix with the help of append_matrix function.
            append_matrix(k,relation,interaction)

        #* Comment 16: Checking if we want to create new population or not.
        elif all(x in matrix[k, 0] for x in population_alc_list[1:]):

            #* Comment 17: Creating new population and combining it with initial.
            new_row = np.array([[[], [], 0]], dtype=object)
            matrix = np.append(matrix, new_row, axis=0)

            #* Comment 18: Appending new population number in the population list.
            population_alc_list.append(len(matrix)-1)

            #* Comment 19: Appending interaction and interation value in the matrix with the help of append_matrix function.
            append_matrix(k,len(matrix)-1,interaction)

    #* Comment 20: Removing the population whose interation is completed.
    population_alc_list.remove(k)

#* Comment 21: Saving the whole matrix in the matrix.txt file.
np.savetxt("matrix.txt", matrix, delimiter=",", fmt='%s')

#* Comment 22: Noting the code ending time.
end = time.time()
end_time = current_time()

#* Comment 23: Printing the Code Runtime.
print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")

#* Comment 24: Checking that random values are in correct propotion.
print("\033[35mExpected\033[00m")

print(f"\033[92mPopulation Number: {rows}\033[00m")

sumofallInteraction = 0
for j in range(rows): sumofallInteraction += matrix[j, 2]
print(f"\033[33m{sumofallInteraction=}\033[00m")

check_pct(int_list,range_list)

new_int_list = []
for l in range(len(matrix)):new_int_list.append(matrix[l, 2])

print("-"*45)

print("\033[35mCreated\033[00m")

print(f"\033[92mPopulation Number: {len(matrix)}\033[00m")

sumofallFINALInteraction = 0
for j in range(rows): sumofallFINALInteraction += len(matrix[j, 0])
print(f"\033[33m{sumofallFINALInteraction=}\033[00m")
print(f"Diff: \033[92m{sumofallFINALInteraction-sumofallInteraction}\033[00m")

acc = check_pct(new_int_list,range_list)

# print(f"\n\t\033[01m\033[34mAccuracy: {acc}%\n\033[00m")