# TODO topological sort

# # Python program to print topological sorting of a DAG
# from collections import defaultdict
#
#
# # Class to represent a graph
# class Graph:
#     def __init__(self, vertices):
#         self.graph = defaultdict(list)  # dictionary containing adjacency List
#         self.V = vertices  # No. of vertices
#
#     # function to add an edge to graph
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#
#     # A recursive function used by topologicalSort
#     def topologicalSortUtil(self, v, visited, stack):
#
#         # Mark the current node as visited.
#         visited[v] = True
#
#         # Recur for all the vertices adjacent to this vertex
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.topologicalSortUtil(i, visited, stack)
#
#         # Push current vertex to stack which stores result
#         stack.insert(0, v)
#
#     # The function to do Topological Sort. It uses recursive
#     # topologicalSortUtil()
#     def topologicalSort(self):
#         # Mark all the vertices as not visited
#         visited = [False] * self.V
#         stack = []
#
#         # Call the recursive helper function to store Topological
#         # Sort starting from all vertices one by one
#         for i in range(self.V):
#             if visited[i] == False:
#                 self.topologicalSortUtil(i, visited, stack)
#
#         # Print contents of stack
#         print(stack)
#



from collections import defaultdict


class Graph:
    def __init__(self, node):
        self.graph = defaultdict(list);
        self.nodes = node;

    def add_edge(self, u, v):
        self.graph[u].append(v);

    def topological_push(self, node, stack, visted_list):
        if (not visted_list[node]):
            visted_list[node] = True;

            for child in self.graph[node]:
                self.topological_push(child, stack, visted_list);

            # stack.append(node);
            stack.insert(0, node);

    def topological_sort(self):
        visited_list = [False] * self.nodes;
        stack = [];

        for i in range(self.nodes):
            self.topological_push(i, stack, visited_list);

        return stack;


while True:
    node, directed_edge = input().strip().split(' ');
    node, directed_edge = [int(node), int(directed_edge)];
    if (node == 0 and directed_edge == 0):
        break;

    g = Graph(node);
    for i in range(directed_edge):
        x, y = input().strip().split(' ');
        x, y = int(x), int(y);
        g.add_edge(x - 1, y - 1);

    res = g.topological_sort();
    res2 = [x + 1 for x in res]
    print(" ".join(map(str, res2)))


    # g = Graph(6)
    # g.add_edge(5, 2);
    # g.add_edge(5, 0);
    # g.add_edge(4, 0);
    # g.add_edge(4, 1);
    # g.add_edge(2, 3);
    # g.add_edge(3, 1);
    #
    # print("Following is a Topological Sort of the given graph")
    # g.topological_sort()


    # 5 4
    # 1 2
    # 2 3
    # 1 3
    # 1 5
    # 0 0
