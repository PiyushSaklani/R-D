import numpy as np

def filter_list(check_list,a,b):
    return len(list(filter(lambda x: a <= x <= b, check_list)))

def check_pct(check_list,range_list):
    for a,b in range_list:
        print(f"Percentage of numbers in the range {a}-{b} : {round(filter_list(check_list,a,b) / len(check_list) * 100,2)}")

range_list = [[100,125],[150,175],[200,250],[300,325],[350,375]]
population_pct = [0.1,0.2,0.5,0.1,0.1]
all_lists, p = [], []

for i,j in zip(range_list,population_pct):
    temp_list = list(range(i[0],i[1]))
    all_lists = all_lists + temp_list
    p = p + [j/len(temp_list)]*len(temp_list)

new_list = np.random.choice(all_lists, size=1000, p=p)

print(new_list)

check_pct(new_list,range_list)