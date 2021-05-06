# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:49:36 2021

@author: ADMIN
"""
import random 



class Agent():
    
    def __init__(self, agents, environment, neighbourhood):
        '''
        This instantiates the class

        Parameters
        ----------
        agents : Number
            These are pseudorandomly generated numbers. 
        environment : Digital numbers rows and columns
            Imported data for the envrionment of our agents
        neighbourhood : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.environment = environment
        self.width=len(environment)
        self.height=len(environment)
        self.y = random.randint(0,self.height)
        self.x = random.randint(0,self.width)
        self.agents = agents
        self.store=0
   
    def __str__(self):
        '''
        This function concatinates the string values of the agents y, x and 
        stored values.
        Returns
        -------
        TYPE String
            List of agents at the different locations and stored values.

        '''
        return 'x=' + str(self.x) + ', y=' + str(self.y) + ', store=' + str(self.store)    
  
    def move(self):
        '''
        This functions adjusts the position of the agents (y,x) shuffling
        randomly increasing or decreasing.

        Returns
        -------
        None.

        '''
        
        if random.shuffle(self.agents):
            self.y = (self.y + 1) % self.height
        else:
            self.y = (self.y - 1) % self.height
            
        if random.shuffle(self.agents):
            self.x = (self.x + 1) % self.width
        else:
            self.x = (self.x - 1) % self.width
            
    def eat(self):
        '''
        This functins allows the agents to eat and store some values 
        if it is more than 10 it gets 10 else it stores what is left
        

        Returns
        -------
        None.

        '''
      
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
        else:
         
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            print(str(self))
            self.store = 0
       
                      
    def share_with_neighbours(self, neighbourhood):
        '''
        This allows for searching and sharing of resources 
        within neighbours

        Parameters
        ----------
        neighbourhood : Assigned variable for the neighbourhood
        
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        '''
        Distance between 

        Parameters
        ----------
        agent : Number
            DESCRIPTION.

        Returns
        -------
        TYPE A number
            The distance between agents i the environment

        '''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
 
   
    #def distance_between(self):
        