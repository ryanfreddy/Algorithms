#Project for Ryan Fredrickson

#Set up a class for jobs
class project:
    def __init__(self,num, begin, end, dollar):
        self.end = end
        self.dollar = dollar
        self.num = num
        self.begin = begin

# Binary searches the jobs you are givent
def binarysearch(job, start):
    low= 0
    hi = start - 1
    while low <= hi:
        mid = (low + hi)//2
        if job[mid].end <= job[start].begin:
            if job[mid + 1].end <= job[start].begin:
                low = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

# Find the path and amount of dollars made through dynamic programming
def optimize(projects):
    #sort projects by earliest end date to last end date
    projects = sorted(projects, key=lambda j: j.end)
    #Find amount of projects
    pro = len(projects)
    #Set up lists to track path and money made
    path = ["" for _ in range(pro)]
    path[0] = str(projects[0].num)
    solution = [0 for _ in range(pro)]
    solution[0] = projects[0].dollar

    #loop through all projects
    for j in range(1, pro):
        money = projects[j].dollar
        projpath = str(projects[j].num)
        ind = binarysearch(projects, j)
        if (ind != -1):
            projpath = path[ind] + ' > ' + projpath
            money += solution[ind]
        #See which way gets you most amount of money add to solution
        solution[j] = max(money, solution[j - 1])
        if money>=solution[j-1]:
            path[j]= projpath
        else:
            path[j] = path[j-1]

    #Print out the results
    print("Plan to get maximum profit:"),
    print path[-1]
    print("Maximum porfit $"),
    print solution[-1]


print("Solution for Data 1:")
f="TestData1.txt"
res = []
with open(f, 'r') as file:
    weeks = int(file.readline())  # reads first line
    projects = int(file.readline())  # reads second line
    for l in file:
        res.append(l.strip().split('\t'))
    #Make all items ints
    x = [[int(float(j)) for j in i] for i in res]
    jobs = []
    for n in x:
        #make duration into end time by adding
        n[2] += n[1]
        #create list of projects
        jobs.append(project(n[0], n[1], n[2], n[3]))
optimize(jobs)

print("Solution for Data 2:")
f="TestData2.txt"
res = []
with open(f, 'r') as file:
    weeks = int(file.readline())  # reads first line
    projects = int(file.readline())  # reads second line
    for l in file:
        res.append(l.strip().split('\t'))
    #Make all items ints
    x = [[int(float(j)) for j in i] for i in res]
    jobs = []
    for n in x:
        #make duration into end time by adding
        n[2] += n[1]
        #create list of projects
        jobs.append(project(n[0], n[1], n[2], n[3]))
optimize(jobs)

print("Solution for Data 3:")
f="TestData3.txt"
res = []
with open(f, 'r') as file:
    weeks = int(file.readline())  # reads first line
    projects = int(file.readline())  # reads second line
    for l in file:
        res.append(l.strip().split('\t'))
    #Make all items ints
    x = [[int(float(j)) for j in i] for i in res]
    jobs = []
    for n in x:
        #make duration into end time by adding
        n[2] += n[1]
        #create list of projects
        jobs.append(project(n[0], n[1], n[2], n[3]))
optimize(jobs)

print("Solution for Data 4:")
f="TestData4.txt"
res = []
with open(f, 'r') as file:
    weeks = int(file.readline())  # reads first line
    projects = int(file.readline())  # reads second line
    for l in file:
        res.append(l.strip().split('\t'))
    #Make all items ints
    x = [[int(float(j)) for j in i] for i in res]
    jobs = []
    for n in x:
        #make duration into end time by adding
        n[2] += n[1]
        #create list of projects
        jobs.append(project(n[0], n[1], n[2], n[3]))
optimize(jobs)