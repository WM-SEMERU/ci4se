def CSWAP(control, target_1, target_2):
    qubits = [unpack_qubit(q) for q in (control, target_1, target_2)]
    return Gate(name='CSWAP', params=[], qubits=qubits)