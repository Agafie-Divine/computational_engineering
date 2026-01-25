## Adaptive Cruise Control Simulation

This project models and simulates a simplified adaptive cruise control (ACC) system using first-principles vehicle dynamics and rule-based control logic.

### System Model
The vehicle is modeled as a single degree-of-freedom system governed by:
dv/dt = (Fp − c.v²) / m

where;
* dv_dt is acceleration
* Fp is the propulsive force
* c is lumped aerodynamic drag coefficient
* v is velocity
* m is the mass of the car

### Control Strategy
A simplified rule-based cruise controller that adjusts the propulsive force based on the deviation from a desired speed using a tolerance band.

- Fmax: accelerate towards desired velocity
- Fmid: maintain speed
- Fmin: decelerate when overshooting

### Other Features
- Visualization of velocity tracking, force switching, and acceleration response

### Modeling Assumptions
- Longitudinal motion only (1-DOF)
- Flat road
- No rolling resistance
- Instantaneous force response
