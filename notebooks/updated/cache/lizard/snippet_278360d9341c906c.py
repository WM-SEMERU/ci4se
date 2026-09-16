def get_DRAT(delta_x_prime, delta_y_prime, max_ptrm_check):
    L = numpy.sqrt(delta_x_prime ** 2 + delta_y_prime ** 2)
    DRAT = old_div(max_ptrm_check, L) * 100
    return DRAT, L