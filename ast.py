from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('E', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'G': 0
}
def astar(start, goal):
    pq=PriorityQueue()
    pq.put((0, start))
    cost={start:0}
    parent={start:None}

    while not pq.empty():
        current= pq.get()[1]
        if current == goal:
            break
        for neighbor,weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbor not in cost or new_cost<cost[neighbor]:
                cost[neighbor]=new_cost

                priority= new_cost + heuristic[neighbor]
                pq.put((priority,neighbor))
                parent[neighbor]= current

    path=[]
    node=goal

    while node is not None:
        path.append(node)
        node=parent[node]

    path.reverse()

    print("path",path)
    print("cost",cost[goal])

astar('A','G')