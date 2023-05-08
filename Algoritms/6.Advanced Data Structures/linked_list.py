from xml.dom import Node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # write a function to insert element in linked list at beginning
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # write a function to insert data at the end of a linked list
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        p = self.head
        # 1 -> 2 -> 3 -> NONE
        while p.next:
            p = p.next
        p.next = new_node


    # write a function wich will insert data at a position k
    def insert_at_position(self, k, data):
        if k == 0:
            self.insert_beginning(data)
            return
        counter = 0
        p = self.head
        new_node = Node(data)
        while counter < k-1:
            if not p:
                raise Exception("No such position!")
            p = p.next
            counter += 1

        # 1->3 -> 8 -> 5 -> None
        if p:
            new_node.next = p.next
            p.next = new_node
        else:
            raise Exception("No such position")

    #  write a function which will delete element at a specific position
    def remove_position(self, position):
        if not self.head:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        # stop before node to be deleted
        # 1 -> 3 -> None
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                raise Exception("No elem at that position")

        if temp.next is None:
            raise Exception("No elem")

        nextElem = temp.next.next
        temp.next = None
        temp.next = nextElem

    # write a function to print all elements of linked list
    def print_lista(self):
        if not self.head:
            return
        p = self.head
        while p:
            print(p.data, end= " ")
            p = p.next
        print("")

    # write a function to find an elem in linked list
    def find_elem(self, elem):
        if not self.head:
            return False
        p = self.head
        while p:
            if p.data == elem:
                return True
            p = p.next
        return False

    # write a function to reverse linked list
    # 1 -> 3 -> 5 ->nxt
    # None <- 1  <- 3 <- 5
    def inverse_list(self):
        if not self.head and not self.head.next:
            return
        prev, actual, nxt = None, self.head, self.head
        while actual:
            nxt = actual.next
            actual.next = prev
            prev = actual
            actual = nxt

        self.head = prev




if __name__ == '__main__':
    lista_mea = LinkedList()
    lista_mea.insert_beginning(3) # 3
    lista_mea.insert_beginning(4) # 4->3

    lista_mea.insert_end(7) #4 3 7
    lista_mea.insert_beginning(2) # 2 4 3 7
    lista_mea.insert_end(8) # 2 4 3 7 8
    # lista_mea.print_lista()
    lista_mea.insert_at_position(4, 5) # 2 4 3 7 8 5
    # lista_mea.remove_position(4) # 2 4 3 7 8
    # print(lista_mea.find_elem(8))
    lista_mea.print_lista()
    lista_mea.inverse_list()
    lista_mea.print_lista() # 8 7 3 2
