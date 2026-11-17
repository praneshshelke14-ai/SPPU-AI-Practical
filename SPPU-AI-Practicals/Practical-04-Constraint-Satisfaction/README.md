# Practical 04 Constraint Satisfaction
## Implementation of Constraint Satisfaction Problem (CSP) in AI

## Aim
Implement a CSP solution for a real-world style problem such as map colouring, Sudoku or timetable scheduling, using backtracking and constraints.

## Problem statement
Implement a Constraint Satisfaction Problem in AI. The notebook mentions map colouring, Sudoku and timetable scheduling and calls out backtracking and constraint programming.

## Objectives
- Understand CSP variables, domains and constraints.
- Study recursion, backtracking, forward checking and consistency.
- Understand MRV and LCV heuristics.
- Apply CSP ideas to map colouring, Sudoku and timetable scheduling.

## Theory
1. A CSP consists of variables, domains and constraints. A solution assigns a value to every variable while satisfying all constraints.
2. In map colouring, each region is a variable, available colours form its domain, and neighbouring regions must have different colours.
3. Backtracking assigns one variable at a time. If an assignment causes a conflict, the algorithm undoes it and tries another value.
4. Forward checking removes values that are no longer possible for neighbouring unassigned variables and detects failure early.
5. MRV (Minimum Remaining Values) selects the unassigned variable with the fewest legal values. LCV (Least Constraining Value) tries the value that restricts neighbours least.

## Algorithm / Procedure
1. Define map regions as variables, colours as domains and neighbouring relationships as constraints.
2. Select an unassigned region using MRV.
3. Order its legal colours using LCV.
4. Assign one colour and run forward checking.
5. If all unassigned regions still have at least one legal colour, recursively assign the next region.
6. If a conflict is found, remove the assignment and try the next colour.
7. Stop when all regions are assigned or no solution is possible.

## Complexity / Practical nature
Backtracking CSP search is exponential in the number of variables in the worst case. MRV, LCV and forward checking are heuristics/propagation methods that reduce the search in many practical cases but do not remove the worst-case exponential bound.

## Expected output / record
The program prints a valid colour for each region in the Australia map-colouring example and verifies that every pair of neighbouring regions has different colours.

## Python program
Source file: [`practical_04_csp_map_coloring.py`](practical_04_csp_map_coloring.py)

### Run
```bash
python practical_04_csp_map_coloring.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_04_csp_map_coloring.py`](practical_04_csp_map_coloring.py) so it can be run directly.

```python
"""Practical 4: Map colouring as a CSP using backtracking, MRV, LCV and forward checking."""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
COLORS = ["Red", "Green", "Blue"]
NEIGHBORS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

assignment = {}


def legal_values(variable):
    used = {assignment[n] for n in NEIGHBORS[variable] if n in assignment}
    return [color for color in COLORS if color not in used]


def select_mrv():
    """Minimum Remaining Values: select the variable with fewest legal colours."""
    unassigned = [v for v in VARIABLES if v not in assignment]
    return min(unassigned, key=lambda v: (len(legal_values(v)), -len(NEIGHBORS[v])))


def order_lcv(variable, values):
    """Least Constraining Value: try the colour that removes fewest neighbour options."""
    def impact(color):
        affected = 0
        for neighbour in NEIGHBORS[variable]:
            if neighbour not in assignment and color in legal_values(neighbour):
                affected += 1
        return affected
    return sorted(values, key=impact)


def forward_check():
    """Fail early if any unassigned variable has no remaining legal colour."""
    return all(legal_values(v) for v in VARIABLES if v not in assignment)


def backtrack():
    if len(assignment) == len(VARIABLES):
        return True

    variable = select_mrv()
    for color in order_lcv(variable, legal_values(variable)):
        assignment[variable] = color
        if forward_check() and backtrack():
            return True
        del assignment[variable]  # undo assignment (backtracking)
    return False


def main():
    if backtrack():
        print("Map-colouring solution:")
        for region in VARIABLES:
            print(f"{region}: {assignment[region]}")
        print("\nConstraint check:", all(
            assignment[a] != assignment[b]
            for a in VARIABLES for b in NEIGHBORS[a]
        ))
    else:
        print("No solution exists with the selected colours.")


if __name__ == "__main__":
    main()
```

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is a CSP?**
Answer: A problem defined by variables, domains and constraints.

**Q2. What are variables in map colouring?**
Answer: The map regions.

**Q3. What is a domain?**
Answer: The set of allowed values for a variable, such as Red, Green and Blue.

**Q4. What is a constraint?**
Answer: A condition that restricts which combinations of values are allowed.

**Q5. What is backtracking?**
Answer: A search technique that assigns values and undoes an assignment when it leads to failure.

**Q6. What is forward checking?**
Answer: After an assignment, it removes inconsistent values from neighbouring unassigned variables and detects empty domains.

**Q7. What is MRV?**
Answer: Minimum Remaining Values: choose the variable with the fewest legal values remaining.

**Q8. What is LCV?**
Answer: Least Constraining Value: choose the value that rules out the fewest choices for neighbouring variables.

**Q9. Why can CSP search become expensive?**
Answer: The number of possible assignments can grow exponentially with the number of variables.

**Q10. Give examples of CSP applications.**
Answer: Map colouring, Sudoku, exam timetabling, staff scheduling and resource allocation.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.
