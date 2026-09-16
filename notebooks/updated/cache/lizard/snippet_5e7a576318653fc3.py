def square_edge_grill(alpha, l=None, Dh=None, fd=None):
    r
    if Dh and l and fd and l > 50 * Dh:
        return (0.5 * (1 - alpha) + (1 - alpha ** 2) + fd * l / Dh
            ) / alpha ** 2
    else:
        return (0.5 * (1 - alpha) + (1 - alpha ** 2)) / alpha ** 2