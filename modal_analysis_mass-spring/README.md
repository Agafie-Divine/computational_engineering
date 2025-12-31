## Modal Analysis of a Multi-DOF Mass-Spring system
This project uses scientific computing to interpret and visualize the natural frequencies and mode shapes of a multi-degree-of-freedom mass-spring system.

## Computational Approach
* Vector and matrix initilaization
* Assembly of stiffness and mass matrices
* Eigenvalue and eigenvector computation
* Mode shape normalization
* Visualization of mode shapes

## Physical System Description
* Five discrete lumped masses
* Six linear springs
* Uniform spring stiffness
* Fixed boundary conditions (end springs to wall)

## Static Equilibrium Solution
The project first assumes static equilibrium with:
\[
\mathbf{f} = \mathbf{K}\mathbf{u}
\]
* Force vector**f**: A column vector of forces applied to each of the masses. 
* Displacement vector**u**: A column vector of resulting displacement of each mass after applied force. 
* Stiffness matrix**K**: Matrix desribing the elastic coupling between masses

## Dynamic Model and Modal Analysis
To study the vibration characteristics of the system:
\[
\mathbf{M}\ddot{\mathbf{u}} + \mathbf{K}\mathbf{u} = 0
\]
* Mass matrix**M**

And assuming harmonic motion, the generalized eigenvalue problem to yield natural frequencies and corresponding mode shapes:
\[
\mathbf{K}\boldsymbol{\phi} = \omega^2 \mathbf{M}\boldsymbol{\phi}
\]

## Results and Engineering Imterpretation
The analysis produces five distinct mode shapes, which corresponds to the five degree of freedoms of the system.
The first mode represents a low-frequency motion where all masses move in the same direction, analogous to body bounce in vehicle dynamics.
Higher modes exhibit increasing numbers of nodes and alternating displacement patterns, indicating localized deformation and higher-frequency behavior.
Understanding these vibration modes is essential for:
* Avoiding resonance
* Improving ride comfort
* Reducing structural fatigue
