def avg_gate_fidelity(self, reference_unitary):
    process_fidelity = self.process_fidelity(reference_unitary)
    dimension = self.pauli_basis.ops[0].shape[0]
    return (dimension * process_fidelity + 1.0) / (dimension + 1.0)