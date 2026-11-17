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
