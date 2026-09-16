def compute_expansion_alignment(satz_a, satz_b, satz_c, satz_d):
    zeta_a = satz_a
    zeta_b = satz_b
    phi_a = compute_phi(zeta_a)
    phi_b = compute_phi(zeta_b)
    theta_a = compute_theta(zeta_a, phi_a)
    theta_b = compute_theta(zeta_b, phi_b)
    phi = (phi_a + phi_b) / 2
    zeta = compute_zeta(phi)
    theta = compute_theta(zeta, phi)
    c_expansion = 4 * (((theta_a + theta_b) / 2 - theta) / (theta_a - theta_b))
    sin_beta_2 = scan_width / (2 * H)
    d = ((R + H) / R * np.cos(phi) - np.cos(zeta)) * sin_beta_2
    e = np.cos(zeta) - np.sqrt(np.cos(zeta) ** 2 - d ** 2)
    c_alignment = 4 * e * np.sin(zeta) / (theta_a - theta_b)
    return c_expansion, c_alignment