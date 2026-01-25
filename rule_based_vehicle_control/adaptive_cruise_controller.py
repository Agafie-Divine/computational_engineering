# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 14:58:10 2026

@author: HP

Project: Rule-Based Adaptive Cruise Control (ACC)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#%%
def vehicle_dynamics(t, y, params):
    '''
    Defines the ODE for the vehicle dynamics

    Args:
    t (float): Time(the solver requires ths
        though it's not used in our simple model)
    y(array): State variable
    Fp (float): Propulsive force
    m (float): Vehicle mass
    c (float): Drag coefficient

    Returns:
        array: The derivative of the state vector, [dv/dt].

    '''
    m, c, v_set, tol, Fmid, Fmax, Fmin = params
    v = y[0]
    Fp = propulsive_force(v, v_set, tol, Fmid, Fmax, Fmin)
    dv_dt = (Fp - (c*v**2)) / m
    
    return [dv_dt]

#%%
def propulsive_force(v, v_set, tol, Fmid, Fmax, Fmin):
    '''
    Defines the conditions for the engine force.
    
    Args:
        v(float) : current vehicle speed
        v_set(float): Desired speed
        tol(float): Tolrance band
        Fmax: High force
        Fmid: Medium force
        Fmin: Low force
        
    Returns:
        float: Propulsive force, Fp
    '''

    # Condition for High speed
    if v < (v_set - tol):
        return Fmax
    # Condition to maintain speed
    elif (v_set - tol) <= v <= (v_set + tol):
        return Fmid
    # Condition to back off
    else:
        return Fmin
#%%
# ------------- Parameters ----------------
m = 1500.0          #Mass of car(kg)
c = 0.35            #Lumped aerodynamic drag coefficient (N*s^2/m^2)
v_set = 25.0        #m/s
tol =  0.5          #m/s
Fmid = c * v_set**2 #N
Fmax = Fmid*5       #N
Fmin = -500.0       #N


#Simulation parameters
t_start = 0.0  #s
t_end = 120.0  #s
t_span = (t_start, t_end)
t_eval = np.linspace(t_start, t_end, 1201)

# Initial condition
y = [0.0]

params = (m, c, v_set, tol, Fmid, Fmax, Fmin)

# Solution
solution = solve_ivp(fun=vehicle_dynamics, t_span=t_span,\
                     y0=y, t_eval=t_eval, args=(params, ), max_step=0.05, method='RK45')
    
t_plot = solution.t
v_plot_ms = solution.y[0]
v_plot_kmh = np.squeeze(solution.y) * 3.6

Fp = np.array([propulsive_force(vi, v_set, tol, Fmid, Fmax, Fmin) for vi in v_plot_ms])
acceleration = (Fp - c*(v_plot_ms**2)) / m

#%%
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(t_plot, v_plot_ms, label='Simulated Velocity', linewidth=2)
ax.set_title('Adaptive Cruise Control Vehicle', fontsize=16)
ax.axhline(v_set, linestyle='--', linewidth=1, label='Desired speed')
ax.axhline(v_set+tol, linestyle=':', linewidth=1, color='g')
ax.axhline(v_set-tol, linestyle=':', linewidth=1, color='r')
ax.set_xlabel('Time (s)', fontsize=12)
ax.set_ylabel('Speed (m/s)', fontsize=12)
ax.legend()
ax.grid(True)
plt.show()
#%%
fig, ax = plt.subplots(3, 1, figsize=(10,6), sharex=True)

ax[0].plot(t_plot, v_plot_ms, label='Simulated Velocity', linewidth=2)
ax[0].set_title('Adaptive Cruise Control Vehicle', fontsize=16)
ax[0].set_ylabel('Speed(m/s)', fontsize=12)
ax[0].legend()
ax[0].grid(True)

ax[1].plot(t_plot, Fp, label='Simulated Propulsive Force', linewidth=2)
ax[1].set_ylabel('Propulsive Force (N)', fontsize=12)
ax[1].legend()
ax[1].grid(True)

ax[2].plot(t_plot, acceleration, label='Simulated Acceleration', linewidth=2)
ax[2].set_ylabel('Acceleration $(m/s^2)$', fontsize=12)
ax[2].legend()
ax[2].grid(True)
ax[2].set_xlabel('Time(s)', fontsize=12)

plt.tight_layout()
plt.show()