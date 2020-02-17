# COMP560 A1 - BACKTRACKING // Sunnie Kwak
file_ = open("usTestFile.txt", "r")

colors = []
statelist = []
adj = {}
sol = {}
stepcount = [0]
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
        sol.update({x.strip() : ''})
        statelist.append(x.strip())
colored = [''] * len(statelist)
# fill in values (in list form) for adjacency dictionary
for x in file_:
    state = x.split(' ')
    adj[state[0]].append(state[1].strip())
    adj[state[1].strip()].append(state[0])

# method to check if color for state is valid (no adjacent state has the color) 
def valid(i, color):
    stepcount[0] = stepcount[0] + 1
    for adjstate in adj[statelist[i]]:
        if sol[adjstate] == color:
            return False
    return True

def coloring(i):
    if colored[len(colored)-1] != '':
        return True
    for color in colors:
        if valid(i, color) == True:
            sol.update({statelist[i] : color})
            colored[i]=color
            if i + 1 < len(statelist):
                if coloring(i + 1):
                    return True
            else:
                return True
            sol.update({statelist[i] : ''})
    return False


                    

# call coloring with first item in statelist
if coloring(0):
    print(sol)
    print("steps: " + str(stepcount[0]))
else:
    print("no solution")
