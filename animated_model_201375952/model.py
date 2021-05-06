# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:37:04 2021

@author: ADMIN
"""
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.

import random # import random
import math
import operator # This is an operator model
import matplotlib.pyplot 
import agentframework
import csv
import matplotlib.animation 



seed=1
random.seed(seed)

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 20
neighbourhood= 20
agents = []
environment=[]

#Animation code

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Opening the data       
f= open("data.txt",newline = '')
# reading in the csv data
reader= csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    
    rowlist = []    # creating an empty row list for the data 

    for value in row:
        rowlist.append(value)  
    environment.append(rowlist)
    
#print(environment)
f.close()



# Make the agents.


for i in range(num_of_agents):
    agents.append(agentframework.Agent(agents,environment,neighbourhood))
    
for i in range(num_of_agents):
   print(agents[i])
    
#print(agents)
# Move the agents.
carry_on = True
def update(frame_number):
    global carry_on
    fig.clear()
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

#print('After eating and moving')


#for i in range(num_of_agents):
    #print(agents[i])
   
#print(environment)

#print(agents)
#matplotlib.pyplot.xlim(0, 255)
#matplotlib.pyplot.ylim(0, 255)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.show()
    
    
def gen_func(b=[0]):
    a=0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a+=1
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_func)
    #print(distance)




