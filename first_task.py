import math
from time import sleep
delta_t=0.1
def control(state, target, max_vel, max_angle):
    global delta_t
    vector=[target[0]-state[0], target[1]-state[1]]
    module=(vector[0]**2+vector[1]**2)**0.5
    angle=math.acos((vector[0])/(module))
    if target[1]<state[1]:
        angle=-angle
    d_angle=abs(state[2]-angle)
    if d_angle<0.01:
        w=0
        if max_vel*delta_t<=module:
            return (max_vel,w)
        else:
            k=module/(max_vel*delta_t)
            return (max_vel*k, w)

    else:
        v=0
        if max_angle*delta_t<=d_angle:
            if state[2]<angle:
                return (v,max_angle)
            else:
                return (v,-max_angle)
        else:
            k=d_angle/(max_angle*delta_t)
            if state[2]<angle:
                return (v,max_angle*k)
            else:
                return (v,-max_angle*k)
def dist(state,target):
    vector = [target[0] - state[0], target[1] - state[1]]
    module = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    return module
flight_task=[[12,5],[-4,11],[-5,5],[-5,-5],[17,17],[0,0]]
state=[0,0,0,0]
for target in flight_task:
    while dist(state, target) > 0.01:
        v,w = control(state, target, 5, math.pi)
        state[0] += math.cos(state[2])*v*delta_t
        state[1] += math.sin(state[2])*v*delta_t
        state[2] += w*delta_t
        state[3] = v
    print(state)
