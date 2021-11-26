# Distributed CNOT

## Pseudocode

Controller

Input: intial qubit state represented by the angles `phi` and `theta` in the Bloch Sphere representation.
For example, `phi = 0` and `theta = 0.5` represents the `|+>` state.
(Note that `phi` and `theta` are scaled by a factor `pi` in the application code.)

```
e = create_epr(Target)

control_qubit = new_qubit()
rotate_y(control_qubit, theta)
rotate_z(control_qubit, phi)

cnot(control_qubit, e)

m = measure(e)
send_classical(m, Target)

target_m = receive_classical(Target)
if target_m == 1:
  gate_z(control_qubit)

```

Target

Input: intial qubit state represented by the angles `phi` and `theta` in the Bloch Sphere representation.
For example, `phi = 0` and `theta = 0.5` represents the `|+>` state.
(Note that `phi` and `theta` are scaled by a factor `pi` in the application code.)

```
e = create_epr(Controller)

target_qubit = new_qubit()
rotate_y(target_qubit, theta)
rotate_z(target_qubit, phi)

controller_m = receive_classical(Controller)

if controller_m == 1:
  gate_x(e)

cnot(e, target_qubit)
hadamard(e)

m = measure(e)
send_classical(m, Controller)


```