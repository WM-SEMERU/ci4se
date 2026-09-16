def permutation_arbitrary(qubit_inds, n_qubits):
    perm = np.eye(2 ** n_qubits, dtype=np.complex128)
    sorted_inds = np.sort(qubit_inds)
    med_i = len(qubit_inds) // 2
    med = sorted_inds[med_i]
    start = med - med_i
    final_map = np.arange(start, start + len(qubit_inds))[::-1]
    start_i = final_map[-1]
    qubit_arr = np.arange(n_qubits)
    made_it = False
    right = True
    while not made_it:
        array = range(len(qubit_inds)) if right else range(len(qubit_inds))[:
            :-1]
        for i in array:
            pmod, qubit_arr = two_swap_helper(np.where(qubit_arr ==
                qubit_inds[i])[0][0], final_map[i], n_qubits, qubit_arr)
            perm = pmod.dot(perm)
            if np.allclose(qubit_arr[final_map[-1]:final_map[0] + 1][::-1],
                qubit_inds):
                made_it = True
                break
        right = not right
    assert np.allclose(qubit_arr[final_map[-1]:final_map[0] + 1][::-1],
        qubit_inds)
    return perm, qubit_arr[::-1], start_i