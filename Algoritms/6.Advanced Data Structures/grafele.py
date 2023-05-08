import networkx as nx
import matplotlib.pyplot as plt

# Crearea unui obiect graf
G = nx.Graph()

# Adăugarea nodurilor
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Adăugarea muchiilor
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(3, 6)
G.add_edge(4, 7)
G.add_edge(5, 6)
G.add_edge(5, 8)
G.add_edge(6, 7)
G.add_edge(6, 9)

# Desenarea graficului
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

def remove_position(self, position):
    if not self.head:
        return
    temp = self.head
    if position == 0:
        self.head = temp.next
        temp = None
        return
    # stop before node to be deleted
    for i in range(position - 1):
        temp = temp.next
        if temp is None:
            raise Exception("No elem at that position")

    if temp.next is None:
        raise Exception("No elem")

    nextElem = temp.next.next
    temp.next = None
    temp.next = nextElem