class Stack:
    def __init__(self):
        # add a data structure whIch wiLl Store The data (indiciu: 'formeaza cuvant din majuscule' )
        self.data = []

    # write a function which will add an element to stack
    def push(self, elem):
        self.data.append(elem)

    # write a function which will remove the first element from stack, and return it
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("No more elements in the stack")

    # write a function which will return the whole stack
    def get_stack(self):
        return self.data

    def __len__(self):
        return len(self.data)
