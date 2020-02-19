# COMP560 A1 - LOCAL SEARCH // Sunnie Kwak
import random
import time
import fileinput
import operator

file_ = fileinput.input()

colors = []
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
        #statelist.append(x.strip())

# fill in values (in list form) for adjacency dictionary
for x in file_:
    state = x.split(' ')
    adj[state[0]].append(state[1].strip())
    adj[state[1].strip()].append(state[0])

#statelist = sorted(adj, key=lambda k: len(adj[k]), reverse=True)



def coloring():
    changed = True
    while changed:
        # initalize violations dictionary
        violations = {}
        for state in adj.keys():
            violations.update({state: 0})

        changed = False
        sortedstate = []

        # count violations per state
        for state in adj.keys():
            for adjstate in adj[state]:
                if sol[state] == sol[adjstate]:
                    violations.update({state: violations[state] + 1})
        print(violations)
        maxviol = max(violations, key=violations.get)
        maxviol = violations[maxviol]
        print(maxviol)
        if maxviol == 0:
            return True
        for v in violations:
            if violations[v] == maxviol:
                sortedstate.append(v)
        # sort by highest number of violations
        #sortedstate = sorted(violations, key=lambda k: violations[k], reverse=True)
        print(sortedstate)
        # for state in sortedstate: # get state with most violations first
        choice = random.choice(sortedstate)
        if violations[choice] > 0:
            changed = True
            changecolor(choice)
        else: 
            break
        if time.time() > timeout:
            return False
    return True

def changecolor(state):
    stepcount[0] = stepcount[0] + 1
    print(state)
    curin = colors.index(sol[state])
    if curin == len(colors) - 1:
        curin = 0
    else:
        curin = curin + 1
    
    sol.update({state : colors[curin]})               

# call coloring with first item in statelist
if coloring():
    print(sol)
    print("steps: " + str(stepcount[0]))
else:
    print("no solution")
    print("steps: " + str(stepcount[0]))
