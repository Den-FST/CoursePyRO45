"""
### Multithreading ###

###################
+    1. create a function that counts how many numbers can be divided by 3 from 1 to n
+    2. create a function that counts how many numbers can be divided by 7 from 1 to n
+    3. create a function that counts how many numbers are palindrom from 1 to n
+    4. create THREADS to run all 3 functions at the same time
    5. create PROCESSES to run all 3 function at the same time
###################

2. run each point(a, b, c) from ex.2(iterators and generators) using:
	a. threads
	b. processes

"""
import multiprocessing
import threading

def count_div_3(n):
    i = 0
    count_3 = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            # print(i)
            count_3 += 1
    return count_3

def count_div_7(n):
    i = 0
    count_7 = 0
    for i in range(1, n+1):
        if i % 7 == 0:
            # print(i)
            count_7 += 1
    return count_7

def count_palind(n):
    count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count

print(f"Numere divizibile cu 3: {count_div_3(100)}")
print(f"Numere divizibile cu 7: {count_div_7(100)}")
print(f"Total numere palindrom: {count_palind(100)}")



def main():

    ### creating threads ###

    t1 = threading.Thread(target=count_div_3, args=(100000,))
    t2 = threading.Thread(target=count_div_7, args=(100000,))
    t3 = threading.Thread(target=count_palind, args=(100000,))
    # # ### starting threads ###
    t1.start()
    t2.start()
    t3.start()

    # # ### joining threads ###
    t1.join()
    t2.join()
    t3.join()
    ###########################

    ### run by process  ###

    ### creating processes ###
    p1 = multiprocessing.Process(target=count_div_3, args=(2000000,))
    p2 = multiprocessing.Process(target=count_div_7, args=(2000000,))
    p3 = multiprocessing.Process(target=count_palind, args=(2000000,))
    ### starting processes ###
    p1.start()
    p2.start()
    p3.start()
    ### joining processes ###
    p1.join()
    p2.join()
    p3.join()

if __name__ == "__main__":
    main()