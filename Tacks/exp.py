import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap_graph = nx.DiGraph()
    pos_heap = {}
    heap_graph = add_heap_edges(heap_graph, heap_root, pos_heap)

    colors_heap = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels_heap = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos_heap, labels=labels_heap, arrows=False, node_size=2500, node_color=colors_heap)
    plt.show()

def build_min_heap(heap_list):
    min_heap = [HeapNode(value) for value in heap_list]
    for i in range(len(min_heap) // 2 - 1, -1, -1):
        min_heapify(min_heap, i)
    return min_heap

def min_heapify(heap, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i

    if left_child < len(heap) and heap[left_child].val < heap[smallest].val:
        smallest = left_child
    if right_child < len(heap) and heap[right_child].val < heap[smallest].val:
        smallest = right_child

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest)

# Приклад з випадковим списком для побудови купи
heap_list = [2, 5, 8, 9, 12, 7]

# Побудова та відображення мінімальної купи
min_heap_root = build_min_heap(heap_list)
draw_heap(min_heap_root)
