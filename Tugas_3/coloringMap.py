class MapColoring:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        
    def is_consistent(self, var, val, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == val:
                return False
        return True
    
    def backtracking_search(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment
        
        var = None
        for v in self.variables:
            if v not in assignment:
                var = v
                break
                
        for val in self.domains:
            if self.is_consistent(var, val, assignment):
                assignment[var] = val
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
                
        return None

variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
domains = ['red', 'green', 'blue']
neighbors = {'A': ['B', 'C', 'F'],
             'B': ['A', 'C', 'D', 'H', 'F', 'E'],
             'C': ['A', 'B', 'D'],
             'D': ['B', 'C', 'I'],
             'E': ['I', 'J', 'G', 'H', 'B'],
             'F': ['A', 'H', 'B', 'J'],
             'G': ['E'],
             'H': ['B', 'F', 'E'],
             'I': ['E', 'D'],
             'J': ['E', 'F']}

map_coloring = MapColoring(variables, domains, neighbors)
solution = map_coloring.backtracking_search({})
print(solution)
