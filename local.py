# COMP560 A1 - LOCAL SEARCH // Sunnie Kwak
import random
import time
import fileinput

file_ = fileinput.input()

colors = []
statelist = []
adj = {}
sol = {}
stepcount = [0]
timeout = time.time() + 60

# fill in list of colors with colors provided
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        colors.append(x.strip())

# fill in values for the adjacency dictionary & solution dictionary
# and fill in list of states (list of states is just for reference to dictionary)
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        adj.update({x.strip() : []})
        sol.update({x.strip() : colors[random.randint(0,len(colors) - 1)]}) # random assigning of colors to states
        statelist.append(x.strip())
colored = [''] * len(statelist)

# fill in values (in list form) for adjacency dictionary
for x in file_:
    state = x.split(' ')
    adj[state[0]].append(state[1].strip())
    adj[state[1].strip()].append(state[0])

statelist = sorted(adj, key=lambda k: len(adj[k]), reverse=True)


def changecolor(adjstate):
    stepcount[0] = stepcount[0] + 1
    curin = colors.index(sol[adjstate])
    if curin == len(colors) - 1:
        curin = 0
    else:
        curin = curin + 1
    
    sol.update({adjstate : colors[curin]})

def coloring(i):
    if colored[len(colored)-1] != '':
        return True
    changed = True
    while changed:
        changed = False
        for state in statelist:
            for adjstate in adj[state]:
                if sol[state] == sol[adjstate]:
                    changed = True
                    changecolor(adjstate)
        if time.time() > timeout:
            return False
    return True
                    

# call coloring with first item in statelist
if coloring(0):
    print(sol)
    print("steps: " + str(stepcount[0]))
else:
    print("no solution")
    print("steps: " + str(stepcount[0]))
