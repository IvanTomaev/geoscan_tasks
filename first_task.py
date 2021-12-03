def control(state, task, max_vel, max_angle):
    vector=[task[0]-state[0], task[1]-state[1]]
    module=(vector[0]**2+vector[1]**2)**0.5
