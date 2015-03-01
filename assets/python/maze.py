# This is not a random import, it's quite pertinent to the code
import random

# First, we create this maze world
length = 10
density = 0.7
barrier = '+'
space = '_'
r = random.random # nice function pointer
maze = [[barrier if r() > density else space for i in xrange(length)] for j in xrange(length)]

# Let's initialize the start and goal locations
start = (0,0)
maze[start[0]][start[1]] = 'S'
goal = (int(r()*length), int(r()*length))
while goal == (0,0): # we shouldn't make this too easy...
    goal = (int(r()*length), int(r()*length))
maze[goal[0]][goal[1]] = 'G'

# We aught to see the world
def print_maze():
    for row in maze:
        for elem in row:
            print elem,
        print ''
print_maze()

quit()
# Shall we Breadth First Search?
frontier = [start]  # stores what's around our current place
visited = {}        # where have we been?
backpointers = {}   # how do we find the way home?
found = False       # we may finish, never to have found the gold
while len(frontier) > 0:
    visit = frontier[0]
    del frontier[0]
    if maze[visit[0]][visit[1]] == 'G':
        found = True
        break
    visited[visit] = 1
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
    print 'No path found :('
else:
    back = backpointers[goal]
    path = []
    while back != start:
        path.append(back)
        back = backpointers[back]

    for step in path:
        maze[step[0]][step[1]] = '@'
    print 'Path of length %d found!' % len(path)
    print_maze()
