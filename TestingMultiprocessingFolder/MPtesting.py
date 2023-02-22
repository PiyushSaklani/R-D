# import multiprocessing as mp

# def h():
#     print("Hello")


# if __name__ == "__main__":

#     process = []
#     pid = []
#     for _ in range(10):
#         p = mp.Process(target=h())
#         p.start()
#         process.append(p)
#         pid.append(p.pid)

#     for prcs in process:
#         prcs.join()

#     print(process)
#     print(pid)


#!---------------------------------------


import multiprocessing
import random
import time

start = time.time()

def process_func(pid,p):
    global data
    a = int(len(data)/p)
    for i in range(a):
        x = a*pid+i
        for j in range(data[x][2]):
            data[x][0].append(random.randint(10,100))
            data[x][1].append(random.randint(1,3))
        
        if x == len(data)-1 :
            return data


global data

data = []
for _ in range(1000000):
    data.append([[],[],random.randint(10,100)])

# print(data)

print(len(data))

if __name__ == '__main__':
    p = 5
    # create a pool of 10 processes
    pool = multiprocessing.Pool(processes=p)

    # apply process_func to each data item in a separate process
    results = []
    for pid in range(p):
        result = pool.apply_async(process_func, (pid,p))
        if result.get() != None:
            for i in result.get():
                print(i)

    # retrieve the results
    # for result in results:
    #     print(result.get())
    #     print()

end = time.time()

print(f"\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")