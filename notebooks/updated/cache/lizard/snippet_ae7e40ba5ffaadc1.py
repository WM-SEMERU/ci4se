def get_default_qubit_mapping(program):
    fake_qubits, real_qubits, qubits = _what_type_of_qubit_does_it_use(program)
    if real_qubits:
        warnings.warn(
            "This program contains integer qubits, so getting a mapping doesn't make sense."
            )
        return {q: q for q in qubits}
    return {qp: Qubit(i) for i, qp in enumerate(qubits)}