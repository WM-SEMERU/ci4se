def unit_normal(pt_a, pt_b, pt_c):
    x_val = np.linalg.det([[1, pt_a[1], pt_a[2]], [1, pt_b[1], pt_b[2]], [1,
        pt_c[1], pt_c[2]]])
    y_val = np.linalg.det([[pt_a[0], 1, pt_a[2]], [pt_b[0], 1, pt_b[2]], [
        pt_c[0], 1, pt_c[2]]])
    z_val = np.linalg.det([[pt_a[0], pt_a[1], 1], [pt_b[0], pt_b[1], 1], [
        pt_c[0], pt_c[1], 1]])
    magnitude = (x_val ** 2 + y_val ** 2 + z_val ** 2) ** 0.5
    mag = x_val / magnitude, y_val / magnitude, z_val / magnitude
    if magnitude < 1e-08:
        mag = 0, 0, 0
    return mag