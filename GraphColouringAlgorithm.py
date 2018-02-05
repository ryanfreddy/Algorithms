from collections import defaultdict
#Assignment 2(380): Ryan Fredrickson 
# Following imports all the graphs into dictionaries of lists
filename="Graph1.txt"
gData1 = defaultdict(list)  # Create dictionary of lists
with open(filename, 'r') as file:
    num = int(file.readline())  # reads first line
    for line in file:
        edited_line = line.replace(":", "").split()
        for each_neighbour in edited_line:
            if each_neighbour != edited_line[0]:
                gData1[int(edited_line[0])].append(int(each_neighbour))

filename="Graph2.txt"
gData2 = defaultdict(list)  # Create dictionary of lists
with open(filename, 'r') as file:
    num = int(file.readline())  # reads first line
    for line in file:
        edited_line = line.replace(":", "").split()
        for each_neighbour in edited_line:
            if each_neighbour != edited_line[0]:
                gData2[int(edited_line[0])].append(int(each_neighbour))


filename="Graph3.txt"
gData3 = defaultdict(list)  # Create dictionary of lists
with open(filename, 'r') as file:
    num = int(file.readline())  # reads first line
    for line in file:
        edited_line = line.replace(":", "").split()
        for each_neighbour in edited_line:
            if each_neighbour != edited_line[0]:
                gData3[int(edited_line[0])].append(int(each_neighbour))

filename="Graph4.txt"
gData4 = defaultdict(list)  # Create dictionary of lists
with open(filename, 'r') as file:
    num = int(file.readline())  # reads first line
    for line in file:
        edited_line = line.replace(":", "").split()
        for each_neighbour in edited_line:
            if each_neighbour != edited_line[0]:
                gData4[int(edited_line[0])].append(int(each_neighbour))

filename="Graph5.txt"
gData5 = defaultdict(list)  # Create dictionary of lists
with open(filename, 'r') as file:
    num = int(file.readline())  # reads first line
    for line in file:
        edited_line = line.replace(":", "").split()
        for each_neighbour in edited_line:
            if each_neighbour != edited_line[0]:
                gData5[int(edited_line[0])].append(int(each_neighbour))


def twocolour(graph):
    coloured = {}                           #creates dictionary of lists
    coloured[1]=0                           #Sets first vertex to one colour
    for a in graph:                         #Loop through all vertices
        if a not in coloured:               #If vertex is not in coloured then graph disconnected
            print "Graph is disconnected"
        else:
            colour = coloured[a]            #set current colour equal to the vertexs colour
            for b in graph[a]:              #for every attached vertex
                if b in coloured:           #if attached is already coloured then checkk to see if it is the same colour
                    if colour == coloured[b]:
                        print "Cannot be two coloured"  #If same colour then the graph cannot be two coloured and exit
                        return
                else:
                    if colour==1:           # Else set the colour to be oppposite of current colour
                        coloured[b]=0
                    else:
                        coloured[b]=1
    print "First number is vertex and second is colour"
    print(coloured)                         #print coloured dictionary


#Easy Colour O(n^2) for the two for loops and the sorting is O(nlog(n)) therefore the computational complexity is o(n^2)
def easyColour(dat):
    sortedlist=[]               #Will contain a list of vertices from most edges to least
    colours={}                  #Will contain vertices with associated colour
    amountofcolours=0           #Will be calculated at the end once the vertices have been given colours

    for k in sorted(dat, key=lambda k: len(dat[k]), reverse=True):  #Sort list
        sortedlist.append(k)

    for c in sortedlist:        #loop from most edges to least
        cols=[]                 #list to hold colours already used
        colr=1                  #first colour chould be 1
        for v in dat[c]:        #loop through adjacent vertices in the graph
            if v in colours:    #If vertex is already in colours add it to the temporary cols
                cols.append(colours[v])

        for colr in cols:     #find the minimum colour required
            colr += 1

        colours[c] = colr

        if colr>amountofcolours:        #if current colour grater than current max make current max
            amountofcolours=colr

    print amountofcolours
    print colours

print "Two colour Graph 1:"
twocolour(gData1)
print "Two colour Graph 2:"
twocolour(gData2)

print "Easy colour Graph 3:"
easyColour(gData3)
print "Easy colour Graph 4:"
easyColour(gData4)
print "Easy colour Graph 5:"
easyColour(gData5)
