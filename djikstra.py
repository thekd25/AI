import heapq

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 2), ('E', 5)],
    'C': [('B', 2), ('D', 4)],
    'D': [('E', 1)],
    'E': []
}

def dijkstra(graph, start):
    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, current = heapq.heappop(pq)

        for neighbor, weight in graph[current]:
            new_distance = dist + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distance

start_node = 'A'

result = dijkstra(graph, start_node)

print("Shortest distances from", start_node)

for node in result:
    print(node, ":", result[node])