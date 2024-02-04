import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_order):
    if tree_root is None:
        return

    tree_graph = nx.DiGraph()
    pos_tree = {tree_root.id: (0, 0)}
    color_mapping = {}

    def dfs(node, depth):
        if node is not None:
            color = "#{:02X}{:02X}{:02X}".format(
                255 - depth * 20, 255 - depth * 20, 255 - depth * 20
            )
            color_mapping[node.id] = color

            if traversal_order == "dfs" and node.left:
                tree_graph.add_edge(node.id, node.left.id)
            if traversal_order == "dfs" and node.right:
                tree_graph.add_edge(node.id, node.right.id)

            dfs(node.left, depth + 1)

            if traversal_order == "bfs" and node.left:
                tree_graph.add_edge(node.id, node.left.id)
            if traversal_order == "bfs" and node.right:
                tree_graph.add_edge(node.id, node.right.id)

            dfs(node.right, depth + 1)

    dfs(tree_root, 0)

    tree_graph = add_edges(tree_graph, tree_root, pos_tree)

    colors_tree = [color_mapping[node[0]] for node in tree_graph.nodes(data=True) if color_mapping.get(node[0])]
    labels_tree = {node[0]: node[1]['label'] for node in tree_graph.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(tree_graph, pos=pos_tree, labels=labels_tree, arrows=True, node_size=2500, node_color=colors_tree)
    plt.show()

if __name__ == "__main__":
    tree_root = Node(0)
    tree_root.left = Node(4)
    tree_root.left.left = Node(5)
    tree_root.left.right = Node(10)
    tree_root.right = Node(1)
    tree_root.right.left = Node(3)

    # Здійснюємо обхід у глибину (DFS)
    draw_tree(tree_root, traversal_order="dfs")

    # Здійснюємо обхід у ширину (BFS)
    draw_tree(tree_root, traversal_order="bfs")
