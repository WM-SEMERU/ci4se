def _recursive_builder(self, operation, gate_name, control_qubits, target_qubit
    ):
    control_true = np.kron(ONE_PROJECTION, operation)
    control_false = np.kron(ZERO_PROJECTION, np.eye(2, 2))
    control_root_true = np.kron(ONE_PROJECTION, sqrtm(operation, disp=True))
    controlled_gate = control_true + control_false
    controlled_root_gate = control_root_true + control_false
    sqrt_name = self.format_gate_name(SQRT_PREFIX, gate_name)
    controlled_subprogram = pq.Program()
    control_gate = pq.Program()
    if len(control_qubits) == 1:
        if gate_name == NOT_GATE_LABEL:
            control_name = CONTROL_PREFIX + gate_name
        else:
            control_name = self.format_gate_name(CONTROL_PREFIX, gate_name)
        control_gate = self._defgate(control_gate, control_name,
            controlled_gate)
        control_gate.inst((control_name, control_qubits[0], target_qubit))
        return control_gate
    else:
        control_sqrt_name = self.format_gate_name(CONTROL_PREFIX, sqrt_name)
        control_gate = self._defgate(control_gate, control_sqrt_name,
            controlled_root_gate)
        control_gate.inst((control_sqrt_name, control_qubits[-1], target_qubit)
            )
        n_minus_one_toffoli = self._recursive_builder(NOT_GATE,
            NOT_GATE_LABEL, control_qubits[:-1], control_qubits[-1])
        n_minus_one_controlled_sqrt = self._recursive_builder(sqrtm(
            operation, disp=True), sqrt_name, control_qubits[:-1], target_qubit
            )
        controlled_subprogram += control_gate
        controlled_subprogram += n_minus_one_toffoli
        controlled_subprogram += control_gate.dagger()
        controlled_subprogram += n_minus_one_toffoli.instructions
        controlled_subprogram += n_minus_one_controlled_sqrt
        return controlled_subprogram