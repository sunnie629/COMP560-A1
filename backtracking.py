# COMP560 A1 - BACKTRACKING SEARCH // Sunnie Kwak
import fileinput

file_ = fileinput.input() # reading file from STDIN

colors = [] # list of colors
adj = {} # adjancency dictionary
statelist = [] # used for easy indexed reference to states
sol = {} # solution dictionary that will be printed at the end
stepcount = [0] # steps counter that will be printed at the end

# fill list of colors with colors provided
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        colors.append(x.strip())

# populate keys for the adjacency dictionary & solution dictionary
# and fill list of states (list of states is just for reference to dictionary)
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        adj.update({x.strip() : []})
        sol.update({x.strip() : ''})

# fill values (in list form) for adjacency dictionary
# fill values so they go both ways (i.e. SA: NSW -> NSW: SA)
for x in file_:
    state = x.split(' ')
    adj[state[0]].append(state[1].strip())
    adj[state[1].strip()].append(state[0])

statelist = sorted(adj, key=lambda k: len(adj[k]), reverse=True) # list of states, sorted by number of adjacent states (highest first)

def coloring(i):
    for color in colors: # loop through color options
        if valid(i, color): # if valid (current color does not match with any adjacent state), assign that color to the state
            sol.update({statelist[i] : color})
            if i + 1 < len(statelist): 
                if coloring(i + 1): # recursively call method to look at next state in array
                    return True
            else: # stops when i has gone through all states
                return True
            sol.update({statelist[i] : ''}) # if backtracked, get rid of color assignment to current state
    print(sol)
    return False # if all possibilities are exhausted and not all states have valid colors, return False

# checks if color for state is valid (no adjacent state has the color) 
# if invalid, return False; else, return True
def valid(i, color):
    stepcount[0] = stepcount[0] + 1
    for adjstate in adj[statelist[i]]: # loops through all adjacent states of current state (statelist[i])
        if sol[adjstate] == color: # if the colors of any adjacent and current state match, return False (invalid)
            return False
    return True # only returns True if no adjacent state has the same color


# if True, solution is found; else, no solution
if coloring(0):
    print(sol)
    print("steps: " + str(stepcount[0]))
else:
    print("no solution")
