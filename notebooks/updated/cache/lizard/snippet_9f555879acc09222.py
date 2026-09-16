def angle_between(u_vec, v_vec):
    u = length_of(u_vec)
    v = length_of(v_vec)
    num = v * u_vec - u * v_vec
    denom = v * u_vec + u * v_vec
    return 2 * arctan2(length_of(num), length_of(denom))