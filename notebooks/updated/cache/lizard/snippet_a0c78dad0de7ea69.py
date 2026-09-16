def run_estimate(unknown_gate, qnum, repetitions):
    qubits = [None] * qnum
    for i in range(len(qubits)):
        qubits[i] = cirq.GridQubit(0, i)
    ancilla = cirq.GridQubit(0, len(qubits))
    circuit = cirq.Circuit.from_ops(cirq.H.on_each(*qubits), [cirq.
        ControlledGate(unknown_gate ** 2 ** i).on(qubits[qnum - i - 1],
        ancilla) for i in range(qnum)], QftInverse(qnum)(*qubits), cirq.
        measure(*qubits, key='phase'))
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)
    return result