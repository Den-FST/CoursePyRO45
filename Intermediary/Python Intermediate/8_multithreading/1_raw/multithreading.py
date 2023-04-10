### Multithreading ###
"""
1. MultiThreading
    Python allows different parts of your code to be executed simultaneously by using threads. 
    They are sequences of program statements that can be executed independently of the rest of the code. 
    We use the threading module for this.

2. GIL (Global Interpreter Lock)
    It only allows one thread to execute at a time. 
    The exceptions are I/O (input/output) operations, as they are not blocked by it. 

3. MultiProcessing
    If we want to parallelize calculations, we can use the multiprocessing module, which runs the code on subprocesses. 
    Each of them gets their own interpreter and memory space, so GIL won't be a problem. 
    Thanks to this, we can use many processors in the computer.
"""

my_name_list = ['bobonete', 'popesco', 'mincu', 'toma', 'micutzu', 'bendeac', 'bucalae']
my_city_list = ['berlin', 'nairobi', 'helsinki', 'bogota', 'tokyo', 'rio', 'moscow']
my_store_list = ['zara', 'h&m', 'c&a', 'decathlon', 'sh', 'adidas', 'hummel']


def main():

    global my_name_list
    global my_city_list
    global my_store_list

    stars = [1, 2, 3, 2, 5, 3, 2]

    ########################################################################################
    ### run one by one ### v1 ###
    
    ########################################################################################

    

    ########################################################################################
    ### run by threads ### v1 ###

    ### creating threads ###

    ### starting threads ###

    ### joining threads ###

    ########################################################################################



    ########################################################################################
    ### run by threads ### v2 ###

    ### creating threads ###

    ### starting threads ###

    ### joining threads ###
    ########################################################################################




    ########################################################################################
    ### run by process ### v2 ###

    ### creating processes ###

    ### starting processes ###

    ### joining processes ###
    ########################################################################################


if __name__ == "__main__":
    main()