# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 05:42:58 2025

@author: HP
"""
#%%
# import all neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

#%%
# Initialize variables
u = np.zeros(5) # displacement vector
f = np.zeros(5) # force vector
K = np.zeros((5,5)) # Stiffness matrix
k = 100 # N/m. Stifness scalar value

#%%
# Fill in the diagonals of the stifness matrix
np.fill_diagonal(K, 2*k)
# Fill in the off-diagonals
for i in range(4):
    for n in range(1,5):
        if i < n:
            K[i,n] = -k
            K[n,i] = -k
            break
        
#%%
# Apply external force
f[2] = 100 # N. Force applied to mass3

# Solve for displacement (f = K@u)
u = np.linalg.solve(K, f)
print(u)

#%%
# Verification
f_check = K @ u
print(f_check)

#%%
# Introoducing the mass matrix. (Mü + Ku = 0)
m = 1 # Kg
M = np.eye(5) * m

# To obtain natural frequencies and mode shapes
# Eigen value : det (K - w²M = 0)
eigvals, eigvecs = np.linalg.eig(np.linalg.inv(M) @ K)
omega = np.sqrt(eigvals) # rad/s

# Sort frequencies
idx = np.argsort(omega)
omega = omega[idx]
modes = eigvecs[:, idx]

#%%
# Visualizing mode shapes
mass_index = np.arange(1, 6)

for p in range(5):
    mode = eigvecs[:, p]
    mode_norm = mode / np.max(np.abs(mode))
    
    plt.figure()
    plt.plot(mass_index, mode_norm, marker='o')
    plt.axhline(0)
    plt.ylim([-1.2, 1.2])
    plt.xlabel('Mass index')
    plt.ylabel('Normalized displacement')
    plt.title(f'Mode {p+1}')
    plt.grid()
    plt.show()