# QKD

## Pseudocode

Alice

Input: number of entangled pairs to generate "n"

```
bases = create n random classical bits
qubits = create n entangled pairs with Bob

for each qubit q[i]:
  if bases[i] == 0:
    outcomes[i] = measure q[i] in standard basis
  else:
    outcomes[i] = measure q[i] in Hadamard basis

wait for message from Bob saying he is done measuring his qubits

send_classical(bases, Bob) 
bases_bob = receive_classical(Bob)

remaining_outcomes = []
for i in 0..n:
  if bases[i] == bases_bob[i]:
    remaining_outcomes += outcomes[i]
  else:
    # discard outcomes[i]

num_remaining = length(remaining_outcomes)
c = fraction of num_remaining

check_indices = c random indices from 0..num_remaining
send_classical(check_indices, Bob)
check_bits_bob = receive_classical(Bob)

num_errors = 0
for each index in check_indices[i]
  if remaining_bits[index] != check_bits_bob[index]:
    num_errors = num_errors + 1

qber = num_errors / c

raw_key = []
for i in 0..num_remaining:
  if i not in check_indices:
    raw_key += remaining_outcomes[i]

return qber, raw_key

```


Bob

Input: number of entangled pairs to generate "n"

```
bases = create n random classical bits
qubits = create n entangled pairs with Alice

for each qubit q[i]:
  if bases[i] == 0:
    outcomes[i] = measure q[i] in standard basis
  else:
    outcomes[i] = measure q[i] in Hadamard basis

send message to Alice saying we are done measuring the qubits

bases_alice = receive_classical(Alice)
send_classical(bases, Alice) 

remaining_outcomes = []
for i in 0..n:
  if bases[i] == bases_alice[i]:
    remaining_outcomes += outcomes[i]
  else:
    # discard outcomes[i]

num_remaining = length(remaining_outcomes)
c = fraction of num_remaining

check_indices = receive_classical(Alice)
check_bits_alice = receive_classical(Alice)

num_errors = 0
for each index in check_indices[i]
  if remaining_bits[index] != check_bits_alice[index]:
    num_errors = num_errors + 1

qber = num_errors / c

raw_key = []
for i in 0..num_remaining:
  if i not in check_indices:
    raw_key += remaining_outcomes[i]

return qber, raw_key

```