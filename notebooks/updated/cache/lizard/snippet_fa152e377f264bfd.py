def do_gate(self, gate: Gate):
    gate_matrix, qubit_inds = _get_gate_tensor_and_qubits(gate=gate)
    self.wf = targeted_tensordot(gate=gate_matrix, wf=self.wf,
        wf_target_inds=qubit_inds)
    return self