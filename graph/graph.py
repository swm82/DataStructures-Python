from collections import deque

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adj_list = {}

    def add_adj(self, v, weight):
        self.adj_list[v] = weight

    def get_adj_list(self):
        return self.adj_list.keys()

    def __str__(self):
        return f'{str(self.key)} - Adjacencies: {str([x.key for x in self.adj_list])}'


class Graph:
    def __init__(self, undirected=False):
        # List of vertices
        self.vert_list = {}
        self.num_vert = 0
        self.undirected = undirected

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        self.num_vert += 1
        return new_vertex

    def get_vertex(self, u):
        return self.vert_list.get(u, None)

    def add_edge(self, u, v, weight=0):
        # adds vertices if not in graph.  Weight as kwarg has def. value
        if u not in self.vert_list:
            self.add_vertex(u)
        if v not in self.vert_list:
            self.add_vertex(v)
        self.vert_list[u].add_adj(self.vert_list[v], weight)
        if self.undirected:
            self.ver_list[v].add_adj(self.vert_list[u], weight)

    def __contains__(self, n):
        return n in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())

    def shortest_path(self, s, e):
        if not self.undirected:
            return self.bfs(s, e)

    def bfs(self, s, e):
        s = self.get_vertex(s)
        e = self.get_vertex(e)
        visited = set()
        parent = {}
        visited.add(s)
        q = deque([s])
        found = False
        while q:
            v = q.popleft()
            if v == e:
                found = True
                break
            for w in v.get_adj_list():
                if w not in visited:
                    parent[w] = v
                    visited.add(w)
                    q.append(w)
        if not found:
            return None
        stack = [e.key]
        path = parent[e]
        while path != s:
            stack.append(path.key)
            path = parent[path]
        stack.append(s.key)
        stack.reverse()
        return ' -> '.join([str(x) for x in stack])




if __name__ == '__main__':
    g = Graph()
    for i in range(10):
        g.add_vertex(i)

    g.add_edge(0,1)
    g.add_edge(0,5)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(4,0)
    g.add_edge(5,2)

    print(g.shortest_path(0, 4))
