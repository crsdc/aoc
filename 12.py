# https://adventofcode.com/2021/day/12

input = []
with open('12data.txt', 'r') as datafile:
    for line in datafile.readlines():
        input.append(tuple(line.strip().split('-')))

# Make each unique cave a dictionary key, and value is its set of connections
graph = {cave: set() for connection in input for cave in connection}
for connection in input:
    graph[connection[0]].add(connection[1])
    graph[connection[1]].add(connection[0])

visited = []
routes = []

def explorefrom(current, rule2status):
    visited.append(current)
    # Check each cave connected to current cave for a viable route
    for candidate in graph[current]:

        # If got all the way to the end, record the route
        if candidate == 'end':
            routes.append(visited + [candidate])

        # If allowed to visit the candidate, do so, and explore from there
        elif candidate not in visited or candidate.isupper():
            explorefrom(candidate, rule2status)

        # Special provision for when a double visit to a small cave is allowed
        elif rule2status and candidate != 'start':
            # If this will be second visit, special rule can't apply beyond it
            if candidate in visited:
                explorefrom(candidate, False)
            else:
                # No double visit yet so keep exploring with rule in place
                explorefrom(candidate, True)

        # Else: this candidate is not allowed, so move on to the next

    # Once all candidates checked, backtrack, but not beyond the start
    if len(visited) > 1:
        visited.pop()

explorefrom('start', False)
print(len(routes))

visited.clear()
routes.clear()
explorefrom('start', True)
print(len(routes))