class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges_to = set()

    def add_edge_to(self, dest):
        self.edges_to.add(dest)
        dest.edges_to.add(self)

    def has_edge_to(self, dest):
        return dest in self.edges_to
        
class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex
  
    def get_vertex(self, name):
        return self.vertices.get(name)

def dfs(graph,current,visited):
    lst = [current.name]
    visited.add(current)
    for neighbor in graph.get_vertex(current.name).edges_to:
        if neighbor not in visited:
            lst += dfs(graph,neighbor,visited)
    return lst

def findpaths(graph,current,visited,depth = 1):
    tot = depth
    visited.add(current)
    for neighbor in graph.get_vertex(current.name).edges_to:
        if neighbor not in visited:
            tot += findpaths(graph,neighbor,visited, depth + 1)
    return tot

a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g1 = Vertex("G")
h = Vertex("H")
i = Vertex("I")

a.add_edge_to(b)
a.add_edge_to(c)
b.add_edge_to(d)
d.add_edge_to(e)
e.add_edge_to(h)
a.add_edge_to(f)
f.add_edge_to(g1)
g1.add_edge_to(i)

g = Graph()
for v in [a, b, c, d, e, f, g1, h, i]:
    g.add_vertex(v)

print(dfs(g,a,set()))
print(findpaths(g,a,set()))