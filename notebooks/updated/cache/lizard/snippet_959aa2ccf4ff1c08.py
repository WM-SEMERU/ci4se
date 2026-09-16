def do_gate_matrix(self, matrix: np.ndarray, qubits: Sequence[int]):
    unitary = lifted_gate_matrix(matrix, list(qubits), n_qubits=self.n_qubits)
    self.wf = unitary.dot(self.wf)
    return self