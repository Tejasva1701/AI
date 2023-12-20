# Write a program to implement AO* Algorithm

import heapq


class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.open = True

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def a_star(start_state, goal_state, get_neighbors, heuristic):
    open_list = []
    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        if not current_node.open:
            continue

        current_node.open = False

        for neighbor in get_neighbors(current_node.state):
            neighbor_node = Node(
                neighbor, current_node, current_node.cost + 1, heuristic(neighbor, goal_state))
            heapq.heappush(open_list, neighbor_node)

    return None


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))


def get_neighbors(state):
    x, y = state
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    # Limiting to a 5x5 grid for this example
    return [(x, y) for x, y in neighbors if 0 <= x < 5 and 0 <= y < 5]


def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)


def block_states(path, get_neighbors):
    blocked_states = set()
    for i in range(len(path) - 1):
        blocked_states.add(path[i])

    def new_get_neighbors(state):
        return [(x, y) for (x, y) in get_neighbors(state) if (x, y) not in blocked_states]

    return new_get_neighbors


if __name__ == "__main__":
    start_state = (0, 0)
    goal_state = (4, 4)

    while start_state != goal_state:
        path = a_star(start_state, goal_state,
                      get_neighbors, manhattan_distance)

        if path:
            print("Path found:", path)
        else:
            print("No path found.")
            break

        # Block the current path and find the next best path
        blocked_states = block_states(path, get_neighbors)
        get_neighbors = blocked_states
        start_state = goal_state  # Reset the start_state for the next iteration

# Sample Output
# Path found: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]

