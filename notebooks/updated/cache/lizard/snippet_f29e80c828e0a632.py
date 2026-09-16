def lifted_gate_matrix(matrix: np.ndarray, qubit_inds: List[int], n_qubits: int
    ):
    n_rows, n_cols = matrix.shape
    assert n_rows == n_cols, 'Matrix must be square'
    gate_size = np.log2(n_rows)
    assert gate_size == int(gate_size), 'Matrix must be 2^n by 2^n'
    gate_size = int(gate_size)
    pi_permutation_matrix, final_map, start_i = permutation_arbitrary(
        qubit_inds, n_qubits)
    if start_i > 0:
        check = final_map[-gate_size - start_i:-start_i]
    else:
        check = final_map[-gate_size - start_i:]
    np.testing.assert_allclose(check, qubit_inds)
    v_matrix = qubit_adjacent_lifted_gate(start_i, matrix, n_qubits)
    return np.dot(np.conj(pi_permutation_matrix.T), np.dot(v_matrix,
        pi_permutation_matrix))