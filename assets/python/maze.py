# This is not a random import, it's quite pertinent to the code
from random import random

# First, we create this maze world
length = 10
density = 0.2  # probability of generating a barrier in a cell
barrier = '+'
space = '_'

def gen_row():
    def gen_cell():
        if random() > 1 - density:
            return barrier
        else:
            return space
    return [gen_cell() for _ in xrange(length)]
maze = [gen_row() for _ in xrange(length)]

# Let's initialize the start and goal locations
start = (0,0)
maze[start[0]][start[1]] = 'S'
def gen_goal():
    return (int(random() * length), int(random() * length))
goal = gen_goal()
while goal == start: # we shouldn't make this too easy...
    goal = gen_goal()
maze[goal[0]][goal[1]] = 'G'

# We ought to see the world
def print_maze():
    for row in maze:
        for elem in row:
            print elem,
        print ''
print_maze()

# Time to Breadth First Search!
frontier = [start]  # stores what's around our current place
visited = {}        # where have we been?
backpointers = {}   # how do we find the way home?
found = False       # we may finish, never to have found the goal

while len(frontier) > 0:
    visit = frontier[0]
    del frontier[0]
    if maze[visit[0]][visit[1]] == 'G':
        found = True
        break
    visited[visit] = 1

    # generate neighbor cells and add them to the frontier
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    neighbors = [tuple(map(sum, zip(x,visit))) for x in neighbors]
    neighbors = filter(lambda x: min(x) >= 0 and max(x) < length, neighbors)
    for n in neighbors:
        if maze[n[0]][n[1]] == barrier:
            continue
        if n not in visited and n not in frontier:
            backpointers[n] = visit
            frontier.append(n)

if not found:
    print '\nNo path found :('
else:
    back = backpointers[goal]
    path = []
    while back != start:
        path.append(back)
        back = backpointers[back]

    for step in path:
        maze[step[0]][step[1]] = '@'
    print '\nPath of length %d found!' % len(path)
    print_maze()
