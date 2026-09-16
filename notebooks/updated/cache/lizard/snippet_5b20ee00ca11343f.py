def controlled(self, control_qubit):
    control_qubit = unpack_qubit(control_qubit)
    self.modifiers.insert(0, 'CONTROLLED')
    self.qubits.insert(0, control_qubit)
    return self