# Trees and Graphs
import heapq


class Tree:
    def __init__(self, elem):
        self.left = None
        self.val = elem
        self.right = None

# print the tree in inorder(SRD)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

# print the tree in postorder (SDR)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


# print the tree in preorder (RSD)
def preorder(root):
    pass

# Checking full binary tree
def isFullTree(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True

#     daca ambii copii nu sunt nuli, return recursiv(pe stange) and recursiv(pe dreapta)
#     else:
#         return something


#  write a function to find the depth of a binary tree
def length(root):
    pass

#  write a function to insert val in a BST
def insert_bst(root, val):
    pass

#  write a function to find if val is in BST
def find_elem(root,val):
    pass


def heap_sort(lst):
    h = []
    for value in lst:
        heapq.heappush(h, value)
    print(h)
    # heapq.heappop(h)
    # print(h)
    return [heapq.heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    # arr = [4,2,5,6,1,2]
    # new_list = heap_sort(arr)
    # print(new_list)

    arbore = Tree(1)
    arbore.left = Tree(2)
    arbore.right = Tree(3)
    #
    arbore.left.right = Tree(4)
    arbore.right.left = Tree(5)
    postorder(arbore)
    print()
    inorder(arbore)
    print()

    '''
              1
           2      3
          9 4    5  6
           x x  x x x x
           
    inordine (SRD) -> 2 4 1 5 3
    postordine(SDR) -> 4 2 5 3 1
    preordine (RSD) -> 1 2 4 3 5
    '''


    # arboreBST = None
    # arboreBST = insert_bst(arboreBST,3)
    # arboreBST = insert_bst(arboreBST, 2)
    # arboreBST = insert_bst(arboreBST, 4)
    # arboreBST = insert_bst(arboreBST, 5)
    # arboreBST = insert_bst(arboreBST, 1)
    # print(find_elem(arboreBST, 5))
    # print(find_elem(arboreBST, 2))
    # print(find_elem(arboreBST, 3))
    # print(find_elem(arboreBST, 66))
