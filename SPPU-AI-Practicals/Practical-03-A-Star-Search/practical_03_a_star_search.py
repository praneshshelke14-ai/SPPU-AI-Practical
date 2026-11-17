"""Practical 3: A* graph search using f(n) = g(n) + h(n)."""
import heapq

# Weighted undirected graph: neighbour -> travel cost
GRAPH = {
    "S": {"A": 2, "B": 4},
    "A": {"S": 2, "C": 2, "D": 6},
    "B": {"S": 4, "C": 1},
    "C": {"A": 2, "B": 1, "G": 3},
    "D": {"A": 6, "G": 1},
    "G": {"C": 3, "D": 1},
}

# Estimated remaining cost to goal G. This example uses an admissible heuristic.
HEURISTIC = {"S": 5, "A": 4, "B": 3, "C": 2, "D": 1, "G": 0}


def a_star(start, goal):
    if start not in GRAPH or goal not in GRAPH:
        raise ValueError("Start and goal must be graph vertices")

    # Heap items are (f_score, g_score, vertex).
    open_heap = [(HEURISTIC[start], 0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    while open_heap:
        f_score, cost_so_far, current = heapq.heappop(open_heap)
        # Ignore outdated heap entries after a better route has been found.
        if cost_so_far != g_cost.get(current):
            continue
        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path)), g_cost[goal]

        for neighbour, edge_cost in GRAPH[current].items():
            new_cost = cost_so_far + edge_cost
            if new_cost < g_cost.get(neighbour, float("inf")):
                g_cost[neighbour] = new_cost
                parent[neighbour] = current
                new_f = new_cost + HEURISTIC[neighbour]
                heapq.heappush(open_heap, (new_f, new_cost, neighbour))

    return None, float("inf")


def main():
    start, goal = "S", "G"
    path, cost = a_star(start, goal)
    print(f"A* search from {start} to {goal}")
    if path is None:
        print("No path found.")
    else:
        print("Best path:", " -> ".join(path))
        print("Total path cost:", cost)


if __name__ == "__main__":
    main()
