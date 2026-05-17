from collections import deque
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

def dfs(node,visited):
    visited.add(node)
    print(node," ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,visited)

# visited=set()
# dfs('A',visited)

def bfs(start):
    visited=set()
    queue=deque()

    visited.add(start)
    queue.append(start)
    while queue:
        node= queue.popleft()
        print(node," ")

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

# bfs('A')

def display_graph():
    print("\nUndirected Graph:")

    for vertex in graph:
        print(vertex, "->", graph[vertex])

# display_graph()

while True:
    print("\n----- MENU -----")
    print("1. Display Graph")
    print("2. DFS Traversal")
    print("3. BFS Traversal")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        display_graph()
    elif choice==2: 
        print("\nDFS Traversal:")
        visited=set()
        dfs('A',visited)
    elif choice==3:
        print("\nBFS Traversal:")
        bfs('A')
    elif choice==4:
        print("Program Exited!")
        quit()
    else:
        print("Enter Correct Input")