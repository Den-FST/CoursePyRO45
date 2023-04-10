### Iterators and Generators ###
"""
1. Normal
2. Iterators
3. Generators
"""

def normal_iteration():

    #############################
    ### list ###
    print("List:")
    a = [1, 2, 3, 4]
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### string ###
    print("String:")
    a = "Alice has a cat"
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### dictionary ###
    print("Dictionary:")
    a = {'name': "Adam", 'surname': "Smith"}
    for key in a:
        print(f"{key}: {a[key]}")
    print("\n\n")
    #############################


def main():

    normal_iteration()
    
    ###########################################################
    ### generate N prime numbers ### normal option ###
    
    ###########################################################


    ###########################################################
    ### generate N prime numbers ### iterator ###
    
    ###########################################################


    ###########################################################
    ### generate N prime numbers ### generator ###
    
    ###########################################################


    ###########################################################
    ### process time ### timeit ###
    
    ###########################################################

if __name__ == "__main__":
    main()