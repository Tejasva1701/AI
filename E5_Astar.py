# Write a program to implement A* Algorithm

import heapq


class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def astar(start_state, goal_state, get_neighbors, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor in get_neighbors(current_node.state):
            neighbor_node = Node(
                neighbor, current_node, current_node.cost + 1, heuristic(neighbor, goal_state))
            heapq.heappush(open_list, neighbor_node)

    return None

# Example usage:


def get_neighbors(state):
    x, y = state
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    # Limiting to a 5x5 grid for this example
    return [(x, y) for x, y in neighbors if 0 <= x < 10 and 0 <= y < 10]


def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    start_state = (5, 6)
    goal_state = (9, 8)
    path = astar(start_state, goal_state, get_neighbors, manhattan_distance)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")

#Sample output
        
#Path found: [(5, 6), (6, 6), (6, 7), (7, 7), (8, 7), (9, 7), (9, 8)]