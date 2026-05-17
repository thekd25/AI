def find(parent,node):
    if parent[node]==node:
        return node
    return find(parent,parent[node])

def union(parent,u,v):
    parent[u]=v

edges=[
    (4,0,1),
    (2,1,2),
    (3,0,3),
    (5,2,3),
    (3,1,3)
]
edges.sort()
vertices=4
parent=[]

for i in range(vertices):
    parent.append(i)
print("Selected Edges:\n")
total_cost=0

for weight, u,v in edges:
    p1=find(parent,u)
    p2=find(parent,v)

    if p1!=p2:
        print(u,"--",v,"=",weight)

        total_cost+=weight
        union(parent,p1,p2)
print("MST:",total_cost)