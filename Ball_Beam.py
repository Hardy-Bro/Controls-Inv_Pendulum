#ball_beam
import gym
import ballbeam_gym
import matplotlib.pyplot as plt
import numpy as np


# pass env arguments as kwargs
kwargs = {'timestep': 0.05, 
          'setpoint': 0.0,
          'beam_length': 1.0,
          'max_angle': 0.5,
          'init_velocity': 0.5,
          'max_timesteps' : 2000,
          'action_mode': 'continuous'}

# create env
env = gym.make('BallBeamSetpoint-v0', **kwargs)
env.reset()

# PID constants
Kp=3.9
Ki=0.002
Kd=0.2
I=0.0

Pos=np.arange(100)
Vel=np.arange(100)
time=np.arange(100)


#running the simulations
for t in range(100):
        env.render()
        pos=env.bb.x
        e=env.bb.x-env.setpoint
        I=I+e
        action=(Kp*e)+(Kd*env.bb.v)
        print (action)
        Pos[t]=env.bb.x-env.setpoint
        Vel[t]=env.bb.v
        time[t]=t+1

        state,reward,done,info=env.step(action)
        if done:
           env.reset()
         
        
plt.subplot(2,1,1)
plt.plot(time,Pos)
plt.title('Position')

plt.subplot(2,1,2)
plt.plot(time,Vel)
plt.title('Velocity')

plt.show()
