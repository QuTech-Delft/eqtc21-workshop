# QKD

## Pseudocode

Alice

Input: number of entangled pairs to generate "n"

```
bases := n random classical bits

qubits := []
for i in 0..n:
  qubits[i] := create_epr(Bob)

outcomes := []
for each qubit q[i]:
  if bases[i] == 0:
    m = measure q[i]
    outcomes[i] := m
  else:
    hadamard(q[i])
    m = measure(q[i])
    outcomes[i] := m

wait for message from Bob saying he is done measuring his qubits

send_classical(bases, Bob) 
bases_bob := receive_classical(Bob)

remaining_outcomes := []
for i in 0..n:
  if bases[i] == bases_bob[i]:
    remaining_outcomes += outcomes[i]
  else:
    # discard outcomes[i]

num_remaining := length(remaining_outcomes)
num_test_indices := n / 4

check_indices := list of random indices from 0..num_remaining (length = num_test_indices)

check_outcomes := []
for each index in check_indices[i]
  check_outcomes += remaining_outcomes[index]:

send_classical(check_indices, Bob)
send_classical(check_outcomes, Bob)
check_outcomes_bob := receive_classical(Bob)

num_errors := 0
for each i in 0..num_test_indices:
  if check_outcomes[i] != check_outcomes_bob:
    num_errors := num_errors + 1

qber := num_errors / num_test_indices

raw_key := []
for i in 0..num_remaining:
  if i not in check_indices:
    raw_key += remaining_outcomes[i]

return qber, raw_key

```


Bob

Input: number of entangled pairs to generate "n"

```
bases := n random classical bits

qubits := []
for i in 0..n:
  qubits[i] := create_epr(Alice)

outcomes := []
for each qubit q[i]:
  if bases[i] == 0:
    m = measure q[i]
    outcomes[i] := m
  else:
    hadamard(q[i])
    m = measure(q[i])
    outcomes[i] := m

send message to Alice saying we are done measuring the qubits

bases_alice := receive_classical(Alice)
send_classical(bases, Alice) 

remaining_outcomes := []
for i in 0..n:
  if bases[i] == bases_alice[i]:
    remaining_outcomes += outcomes[i]
  else:
    # discard outcomes[i]

num_remaining := length(remaining_outcomes)
num_test_indices := n / 4

check_indices := receive_classical(Alice)
check_outcomes_alice := receive_classical(Alice)

check_outcomes := []
for each index in check_indices[i]
  check_outcomes += remaining_outcomes[index]:

num_errors = 0
for each i in 0..num_test_indices:
  if check_outcomes[i] != check_outcomes_alice:
    num_errors := num_errors + 1

qber = num_errors / c

raw_key = []
for i in 0..num_remaining:
  if i not in check_indices:
    raw_key += remaining_outcomes[i]

return qber, raw_key

```