def _next_grav_gsa(grav_initial, grav_reduction_rate, iteration, max_iterations
    ):
    return grav_initial * math.exp(-grav_reduction_rate * iteration / float
        (max_iterations))