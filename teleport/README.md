# Teleportation

## Pseudocode

Sender

Input: qubit to be teleported represented by the angles `phi` and `theta` in the Bloch Sphere representation.
For example, `phi = 0` and `theta = 0.5` represents the `|+>` state.
(Note that `phi` and `theta` are scaled by a factor `pi` in the application code.)

```
q = new_qubit()
rotate_y(q, theta)
rotate_z(q, phi)

e = create_epr(Receiver)

cnot(q, e)
hadamard(q)

m1 = measure(q)
m2 = measure(e)

send_classical(m1, Receiver)
send_classical(m2, Receiver)

```

Receiver

(No inputs)

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