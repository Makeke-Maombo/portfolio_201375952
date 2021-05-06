# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:37:04 2021

@author: ADMIN
"""

# Importation of all the modules, this precedes scripting
import tkinter
import random # import random
#import math
import operator # This is an operator model
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot 
import agentframework
import csv
import matplotlib.animation 
import requests
import bs4 


#Initialize random number genarator
seed=1
random.seed(seed)


# Declaration of variables
num_of_agents = 10
num_of_iterations = 20
neighbourhood= 20
agents = []
environment=[]



def run():
    '''
    This function initialises the running of the model

    Returns
    -------
    None.

    '''
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_func)
    #canvas.show()
    canvas.draw()
    

#Defining the parameters of the matplot figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#GUI code and menubar for dispalying and running of the model
root = tkinter.Tk()
#root.wm_title("Model")
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


#External import of agents(y,x)

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content= r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

#Make the agents, the neighbourhood for sharing, environment and additional 
#data the environment

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents,neighbourhood,y,x))
print(y,x)
    
def print_agents():
    '''
    function to print the agents

    Returns
    -------
    None.

    '''
    for i in range(num_of_agents):
        print(agents[i])
    

# Opening the and copying the data, the environment   
  
f= open("data.txt",newline = '')
# reading in the csv data
reader= csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    
    rowlist = []    # creating an empty row list for the data 

    for value in row:
        rowlist.append(value)  
    environment.append(rowlist)
    
#print(environment)
f.close() # important if 'with' is not used to close the file manually.


#print(agents)

#Distance between agents
def distance_between(agents_row_a, agents_row_b):
    '''
    This computes the distance between agents

    Parameters
    ----------
    agents_row_a : TYPE
        DESCRIPTION.
    agents_row_b : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE Number
        Distance between agents_row_a, agents_row_b

    '''
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


# y,x moving, eating and storing some values
carry_on = True
def update(frame_number):
    '''
    This function sets the model running and agents interacting

    Parameters
    ----------
    frame_number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    global carry_on
    fig.clear()
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

print('After eating and moving')

    
def gen_func(b=[0]):
    '''
    This is the generator function to control the loop and stopping.

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    a : TYPE
        DESCRIPTION.

    '''
    a=0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a+=1
    
    
tkinter.mainloop()


