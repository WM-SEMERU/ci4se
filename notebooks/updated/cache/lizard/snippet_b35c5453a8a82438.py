def calculate_reduced_matrix_elements_0(fine_states):
    factor = sqrt(3 * c ** 3 * me ** 2 * e ** 2 / (16 * Pi * epsilon0 * 
        hbar ** 3))
    einsteinA = get_einstein_A_matrix(fine_states)
    omega_fine = calculate_omega_matrix(fine_states)
    reduced_matrix_elements = [[(0.0) for jj in range(len(fine_states))] for
        ii in range(len(fine_states))]
    for ii in range(len(fine_states)):
        i = fine_states[ii]
        for jj in range(ii):
            j = fine_states[jj]
            t = Transition(i, j)
            einsteinAij = einsteinA[ii][jj]
            omega0 = omega_fine[ii][jj]
            Ji = i.j
            Jj = j.j
            rij = sqrt((2.0 * Ji + 1) / (2 * Jj + 1)) * sqrt(einsteinAij / 
                omega0 ** 3)
            rij = factor * rij
            reduced_matrix_elements[ii][jj] = rij
            reduced_matrix_elements[jj][ii] = rij * (-1) ** (Jj - Ji)
    return reduced_matrix_elements