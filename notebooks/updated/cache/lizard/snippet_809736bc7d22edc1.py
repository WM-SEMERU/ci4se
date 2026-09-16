def hhl_circuit(A, C, t, register_size, *input_prep_gates):
    ancilla = cirq.GridQubit(0, 0)
    register = [cirq.GridQubit(i + 1, 0) for i in range(register_size)]
    memory = cirq.GridQubit(register_size + 1, 0)
    c = cirq.Circuit()
    hs = HamiltonianSimulation(A, t)
    pe = PhaseEstimation(register_size + 1, hs)
    c.append([gate(memory) for gate in input_prep_gates])
    c.append([pe(*(register + [memory])), EigenRotation(register_size + 1,
        C, t)(*(register + [ancilla])), pe(*(register + [memory])) ** -1,
        cirq.measure(ancilla)])
    c.append([cirq.pauli_string_expectation(cirq.PauliString({ancilla: cirq
        .Z}), key='a'), cirq.pauli_string_expectation(cirq.PauliString({
        memory: cirq.X}), key='x'), cirq.pauli_string_expectation(cirq.
        PauliString({memory: cirq.Y}), key='y'), cirq.
        pauli_string_expectation(cirq.PauliString({memory: cirq.Z}), key='z')])
    return c