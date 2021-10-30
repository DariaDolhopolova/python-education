"""This module implements graph with classes Vertex and Graph"""

class Vertex:
    """The class for vertex of the graph, with id and list of all connected elements"""
    def __init__(self, key):
        self.id = key
        self.connected_to = []

    def add_neighbor(self, neighbor):
        """Method to add neighbor to the Vertex"""
        self.connected_to.append(neighbor)

    def get_connections(self):
        """Returns the list of connections to the vertex"""
        return self.connected_to

    def get_id(self):
        """returns id of the vertex"""
        return self.id

    def __str__(self):
        return str(self.id)


class Graph:
    """The class for main graph implementation"""

    def __init__(self):
        self.master_list = {}
        self.totalnum = 0

    def add_vertex(self, key):
        """Method to add vertex to the graph"""
        self.totalnum += 1
        new_vert = Vertex(key)
        self.master_list[key] = new_vert
        return new_vert

    def get_vertex(self, key):
        """method to find vertex in graph, returns vertex obj or None"""
        if key in self.master_list:
            return self.master_list[key]
        return None

    def add_edge(self, vert1, vert2):
        """Method to add the connections between vertices"""
        if vert1 not in self.master_list:
            self.add_vertex(vert1)
        if vert2 not in self.master_list:
            self.add_vertex(vert2)
        self.master_list[vert1].add_neighbor(vert2)
        self.master_list[vert2].add_neighbor(vert1)

    def get_vertices(self):
        """Returns all vertices"""
        return self.master_list.keys()

    def lookup(self, value):
        """Returns vertex with it's connections, if exists."""
        if value in self.master_list:
            connections = self.master_list[value].get_connections()
            return f"{value} <=> {connections}"
        return "No vertex with this value"

    def delete(self, vertex):
        """method to delete vertex and it's connections"""
        if vertex in self.master_list:
            connections = self.master_list[vertex].get_connections()
            for vert in connections:
                index = self.master_list[vert].get_connections().index(vertex)
                self.master_list[vert].get_connections().pop(index)
            self.master_list.pop(vertex, "No such vertex")
        return "No such vertex"

    def __iter__(self):
        return iter(self.master_list.values())

    def __contains__(self, item):
        if item in self.master_list:
            return True
        return False


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    for ver in g:
        print(ver)
    print(g.get_vertices())
    print(g.master_list[0].get_connections())
    g.add_edge(1, 4)
    print(g.master_list[1].get_connections())
    g.delete(1)
    print(g.master_list[0].get_connections())
