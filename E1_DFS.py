# Write a program to implement DFS. 

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def delete_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for adj_node in self.graph:
                self.graph[adj_node] = [
                    n for n in self.graph[adj_node] if n != node]

    #   undirected graph
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        result = []

        if start not in visited:
            result.append(start)
            visited.add(start)
            for neighbor in self.graph[start]:
                result.extend(self.dfs(neighbor, visited))

        return result


def main():
    graph = Graph()

    while True:
        print("\nMenu:")
        print("1. Add Node")
        print("2. Delete Node")
        print("3. Add Edge")
        print("4. DFS Traversal")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            node = input("Enter node to add: ")
            graph.add_node(node)
        elif choice == 2:
            node = input("Enter node to delete: ")
            graph.delete_node(node)
        elif choice == 3:
            node1 = input("Enter first node of the edge: ")
            node2 = input("Enter second node of the edge: ")
            graph.add_edge(node1, node2)
        elif choice == 4:
            start = input("Enter the starting node for DFS traversal: ")
            dfs_result = graph.dfs(start)
            print("DFS Traversal:", " -> ".join(dfs_result))
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Sample input with output
    
# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 2

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 4

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 6

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 3

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 5

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 1
# Enter node to add: 7

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 4
# Enter the starting node for DFS traversal: 2
# DFS Traversal: 2

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 3
# Enter first node of the edge: 2
# Enter second node of the edge: 4

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 3
# Enter first node of the edge: 4
# Enter second node of the edge: 6

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 3
# Enter first node of the edge: 2
# Enter second node of the edge: 3

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 3
# Enter first node of the edge: 3
# Enter second node of the edge: 5

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 3
# Enter first node of the edge: 5
# Enter second node of the edge: 7

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice: 4
# Enter the starting node for DFS traversal: 2
# DFS Traversal: 2 -> 4 -> 6 -> 3 -> 5 -> 7

# Menu:
# 1. Add Node
# 2. Delete Node
# 3. Add Edge
# 4. DFS Traversal
# 5. Quit
# Enter your choice:5
