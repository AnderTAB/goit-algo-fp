import random

def generate_random_graph(num_vertices, max_distance, seed=None):
    if seed is not None:
        random.seed(seed)    
    graph = {}

    vertices = [chr(ord('A') + i) for i in range(num_vertices)]

    for vertex in vertices:
        num_neighbors = random.randint(1, num_vertices - 1)
        neighbors = random.sample(vertices, num_neighbors)
        distances = [random.randint(1, max_distance) for _ in range(num_neighbors)]
        graph[vertex] = dict(zip(neighbors, distances))

    return graph

if __name__ =="__main__":
    random_graph = generate_random_graph(4, 10, seed = 9)
    for gr  in random_graph:
        print(f'{gr} : {random_graph[gr]}')