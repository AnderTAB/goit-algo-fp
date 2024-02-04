import heapq

from random_graph import generate_random_graph

# для кращого тестування розроблено генератор виипадкових графів
graph = generate_random_graph(num_vertices = 4, max_distance = 10, seed = 17)

inf = float('inf')
distances = {vertex: inf for vertex in graph}
distances['A'] = 0


priority_queue = [(0, 'A')]

while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_distance > distances[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex].items():
        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))
       
for gr  in graph:
    print(f'{gr} : {graph[gr]}')           
print("Найкоротші відстані від вершини A:")

for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
    
    
