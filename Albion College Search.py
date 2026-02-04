## NECCESSARY IMPORTS
import matplotlib.pyplot as plt
import networkx as nx

##img = plt.imread("C:/Users/golde/OneDrive/Pictures/Screenshots/ALBION COLLEGE CAMPUS.png")
G = nx.Graph()

G.add_node("Node A")
G.add_node("Node B")

G.add_edge("Node A", "Node B")

##plt.imshow(img)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, edge_color='black', font_size=12)

plt.show()
## Locations

