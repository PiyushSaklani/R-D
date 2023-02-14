import numpy as np

list1 = list(range(100,125))
list2 = list(range(150,175))
list3 = list(range(200,250))
list4 = list(range(300,325))
list5 = list(range(350,375))

# combine all lists into one list
all_lists = list1 + list2 + list3 + list4 + list5

print(all_lists)

# specify the percentages for each list
p = [0.1/len(list1)]*len(list1) + [0.2/len(list2)]*len(list2) + [0.5/len(list3)]*len(list3) + [0.1/len(list4)]*len(list4) + [0.1/len(list5)]*len(list5)

print(p)


# choose elements from the lists according to the percentages
new_list = np.random.choice(all_lists, size=1000, p=p)

print(new_list)

filtered_list = list(filter(lambda x: 100 <= x <= 125, new_list))
percentage = len(filtered_list) / len(new_list) * 100
print("Percentage of numbers in the range 100-125:", percentage)

filtered_list = list(filter(lambda x: 150 <= x <= 175, new_list))
percentage = len(filtered_list) / len(new_list) * 100
print("Percentage of numbers in the range 150-175:", percentage)

filtered_list = list(filter(lambda x: 200 <= x <= 250, new_list))
percentage = len(filtered_list) / len(new_list) * 100
print("Percentage of numbers in the range 200-250:", percentage)

filtered_list = list(filter(lambda x: 300 <= x <= 325, new_list))
percentage = len(filtered_list) / len(new_list) * 100
print("Percentage of numbers in the range 300-325:", percentage)

filtered_list = list(filter(lambda x: 350 <= x <= 375, new_list))
percentage = len(filtered_list) / len(new_list) * 100
print("Percentage of numbers in the range 350-375:", percentage)