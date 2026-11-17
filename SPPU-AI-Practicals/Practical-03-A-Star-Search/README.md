# Practical 03 A Star Search
## Implementation of A* Search Algorithm

## Aim
Implement the A* algorithm to solve an AI search problem using graph search.

## Problem statement
Implement an A* search algorithm to solve an AI search problem using graph search, following the Practical 3 notebook.

## Objectives
- Understand informed or heuristic search.
- Represent a weighted problem as a graph.
- Use path cost and heuristic estimates to select promising states.

## Theory
1. A* is an informed search algorithm that selects the node with the lowest estimated total cost.
2. It uses f(n) = g(n) + h(n), where g(n) is the cost from the start node to n and h(n) estimates the remaining cost from n to the goal.
3. The frontier is maintained as a priority queue. The algorithm updates a node if a less expensive route to it is found.
4. An admissible heuristic never overestimates the true remaining cost. With suitable conditions (including an admissible heuristic and correct graph-search handling), A* can find an optimal path.

## Algorithm / Procedure
1. Initialize the priority queue with the start node and f(start) = h(start).
2. Set g(start) = 0 and record no parent for the start.
3. Remove the frontier node with the smallest f score.
4. If it is the goal, reconstruct the path from the parent links.
5. For each neighbour, calculate tentative_g = g(current) + edge_cost.
6. If tentative_g is better than the recorded cost, update its cost and parent and push it with f = g + h.
7. If the frontier becomes empty, report that no path exists.

## Complexity / Practical nature
A* worst-case time and space are exponential in search depth in general; performance depends strongly on branching factor and heuristic quality. A priority-queue implementation adds logarithmic heap operations per insertion/removal.

## Expected output / record
The supplied graph example returns the path S -> A -> C -> G with total path cost 7.

## Python program
Source file: [`practical_03_a_star_search.py`](practical_03_a_star_search.py)

### Run
```bash
python practical_03_a_star_search.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_03_a_star_search.py`](practical_03_a_star_search.py) so it can be run directly.

```python
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
```

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is informed search?**
Answer: Search that uses additional problem knowledge, usually a heuristic, to guide exploration.

**Q2. What is A*?**
Answer: A best-first search algorithm that orders nodes using f(n) = g(n) + h(n).

**Q3. What is g(n)?**
Answer: The actual path cost from the start node to node n.

**Q4. What is h(n)?**
Answer: An estimate of the remaining cost from node n to the goal.

**Q5. What is f(n)?**
Answer: The estimated total solution cost through n: g(n) + h(n).

**Q6. What is an admissible heuristic?**
Answer: A heuristic that never overestimates the true minimum remaining cost.

**Q7. Which data structure is commonly used for the open list?**
Answer: A priority queue or min-heap.

**Q8. What happens if h(n) = 0 for every node?**
Answer: A* behaves like uniform-cost search.

**Q9. Why store parent links?**
Answer: To reconstruct the final path after reaching the goal.

**Q10. Can A* performance depend on the heuristic?**
Answer: Yes. A more informative admissible heuristic can reduce the number of explored nodes.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.
