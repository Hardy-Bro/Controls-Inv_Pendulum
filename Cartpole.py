#cartpole 

import gym
import matplotlib.pyplot as plt 
import numpy as np
import time
a=time.time()

env_name="CartPole-v1"
env=gym.make(env_name)


class Agent():
    def __init__(self,env):
        self.action_size=env.action_space.n
    
    def get_action(self,state,stateprev):
        omega=state[2]-stateprev
        theta=state[2]
        var=0.005
        f=-var
        g=var
        
        #All the required actions and their required conditions
        if (theta >0 and omega >f):
            action=1
        elif (theta>0 and omega <f):
            action=0
        elif (theta<0 and omega >g):
            action=1
        else:
            action=0
        return (action)


agent=Agent(env)
state=env.reset()
stateprev=0


#Running the simulation
for _ in range (500):
    
    action=agent.get_action(state,stateprev)
    stateprev=state[2]
    state,reward,done,info=env.step(action)
    env.render()
    #stateprev=state[2]
   
    
b=time.time()
#to measure the time duration for which the program runs
print(b-a)

