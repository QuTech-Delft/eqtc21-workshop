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
e = create_epr(Sender)

m1 = receive_classical(Sender)
m2 = receive_classical(Sender)

if m2 == 1:
  x_gate(e)
if m1 == 1:
  z_gate(e)

return e
```