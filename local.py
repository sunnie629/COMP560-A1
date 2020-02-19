# COMP560 A1 - LOCAL SEARCH // Sunnie Kwak
import random
import time
import fileinput
import operator

file_ = fileinput.input() # reading file from STDIN

colors = [] # list of colors
adj = {} # adjancency dictionary
sol = {} # solution dictionary that will be printed at the end
stepcount = [0] # steps counter that will be printed at the end
timeout = time.time() + 60 # one minute timer

# fill list of colors with colors provided
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        colors.append(x.strip())

# fill keys for the adjacency dictionary & solution dictionary
for x in file_:
    if x in ['\n', '\r\n']:
        break
    else:
        adj.update({x.strip() : []})
        sol.update({x.strip() : colors[random.randint(0,len(colors) - 1)]}) # random assigning of initial colors to states

# fill values (in list form) for adjacency dictionary
# fill values so they go both ways (i.e. SA: NSW -> NSW: SA)
for x in file_:
    state = x.split(' ')
    adj[state[0]].append(state[1].strip())
    adj[state[1].strip()].append(state[0])

def coloring():
    changed = True
    while True: # loop runs until no changes have been made
        changed = False
        
        # initalize violations dictionary (will hold the number of violations for each state)
        violations = {}
        for state in adj.keys():
            violations.update({state: 0})

        maxviolstates = [] # list that will hold states with the max number of violations

        # count violations (color is same for current state and adjacent state) per state
        for state in adj.keys():
            for adjstate in adj[state]:
                if sol[state] == sol[adjstate]:
                    violations.update({state: violations[state] + 1})

        # get the highest number of violations (int)
        maxviol = max(violations, key=violations.get)
        if maxviol == 0:
            break
        maxviol = violations[maxviol]
        
        # if the highest number of violations is 0, there are no violations -> return True; solution has been found
        if maxviol == 0:
            return True
        
        # add to maxviolstates only if number of violations == max number (getting the most constrained variables)
        for v in violations:
            if violations[v] == maxviol: 
                maxviolstates.append(v)

        choice = random.choice(maxviolstates) # choose a random state from maxviolstates
        # if violation exists, change color
        changed = True
        changecolor(choice)
        
        if time.time() > timeout: # if program runs for more than a minute, time out & return False
            return False
    return True

# change the color of the state chosen - state chosen will be (one of) the most contrained variable(s)
def changecolor(state):
    stepcount[0] = stepcount[0] + 1
    curin = colors.index(sol[state])
    if curin == len(colors) - 1: # assign color next in index from color array
        curin = 0
    else:
        curin = curin + 1
    
    sol.update({state : colors[curin]}) # update sol dict with new color assigned to state           

# if returned True, solution is found; else, no solution is found
if coloring():
    print(sol)
    print("steps: " + str(stepcount[0]))
else:
    print("no solution")
    print("steps: " + str(stepcount[0]))
