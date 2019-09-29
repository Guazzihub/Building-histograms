 #Setup
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import math
import os

instru = open('instructions.txt').read()

print(instru)
os.system('PAUSE')
os.system('CLS')

sample = open('sample.txt').readlines()

default = [] #default list (table to list)

 #Converting 'sample' into list
for i in range(len(sample)):
        linha = sample[i].strip().split(' ')

        for j in range(len(linha)):
                default.append (int(linha[j]))


classes = [] #List containing every class
 #Calcs
k = (round(math.sqrt(len(default))))
defaultMin = min(default)
defaultMax = max(default)
at = (defaultMax - defaultMin)
h = round(at/k)
interval = (defaultMin + h)
classes.append (defaultMin) #append the first pair of classes.
classes.append (interval)


 #Generating classes
while interval in range(max(default)):
        classes.append(interval) #append [1st
        interval = (interval + h)
        classes.append(interval) #append 2nd class]


 #Counting frequencies
s = 1
r = 0
m = 0

 #Frequency
counterList = []
counter = 0
counterAcum = 0
acumList = [] #Cumulative frequency

 #Relative frequency
relative= 0
relativeAcum = 0
relativeList = []
relativeacumList = [] # Cumulative frequency (relative)

 #Midpoint
midPoint = 0
midpointList = []

 #Calculating table elements in classes and appending every element to its corresponding frequency list
while s < len(classes):
        while m < len(default):
                if default[m] >= classes[r] and default[m] < classes[s]:
                        counter+=1
                        m+=1
                else:
                        m+=1
        counterAcum = counterAcum + counter
        counterList.append(counter) #frequency list generator
        acumList.append(counterAcum) #Cumulative list generator

        relative = counter/len(default)
        relativeAcum = relative + relativeAcum
        relativeList.append (format (relative, '.2f')) #Relative list generator
        relativeacumList.append (format(relativeAcum, '.2f')) #Relative cumulative list generator

        midPoint = (classes[s] + classes[r])/2
        midpointList.append (round((midPoint))) #Midpoint list generator



        r+=2
        s+=2
        m=0
        counter = 0
r=0
classSort = []
 # Generating unique classes
while r in range(len(classes)):
        classSort.append(classes[r])
        r+=2

 #Setting up (table)
fig = go.Figure(data=[go.Table(
        header=dict(values=['Classes' + f' (h={h})', 'Frequency', 'Frequency cumulative', 'Relative frequency', 'Relative frequency (cumulative)', 'Midpoint'],
        line_color='darkslategray',
        fill_color='#D1E8D9',
        align='center'),
        cells=dict(values=[classSort, # 1st column
                        counterList, # 2nd column
                        acumList, # 3rd column
                        relativeList, # 4th column
			relativeacumList, # 5th column
			midpointList, ],# 6th column
                line_color='darkslategray',
                fill_color='#FFFAE6',
                align='center'))

])

 #Showing table
fig.update_layout(width=1200, height=1000)
fig.show()

 #Building the graphic
plt.title('Frequency histogram') # Graph name
plt.xlabel('Classes') #X Label
plt.ylabel('Frequency') #Y Label

plt.bar(classSort,counterList, color='#ff5349')
plt.show()

#Printing default list but ordered
print(sorted(default))
os.system('PAUSE')
