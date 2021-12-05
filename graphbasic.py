
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        #graphs is a recursion data structure
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths
    
    def get_shortest_path(self,start, end, path=[]):
        path = path + [start]
        if start not in self.graph_dict:
            return None
        if start == end:
            return [path]
        shortest = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp
        return shortest




            
routes = [
    ("mumbai", "paris"),
    ("mumbai","dubai"),
    ("paris","dubai"),
    ("paris","new york"),
    ("dubai","new york"),
    ("new york","toronto")
]

route_graphs = Graph(routes)


start = "mumbai"
end = "new york"
print(route_graphs.get_shortest_path(start, end))