def make_bernstein_vazirani_circuit(input_qubits, output_qubit, oracle):
    c = cirq.Circuit()
    c.append([cirq.X(output_qubit), cirq.H(output_qubit), cirq.H.on_each(*
        input_qubits)])
    c.append(oracle)
    c.append([cirq.H.on_each(*input_qubits), cirq.measure(*input_qubits,
        key='result')])
    return c