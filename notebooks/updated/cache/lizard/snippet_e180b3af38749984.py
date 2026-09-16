def compute_elementary_effects(model_inputs, model_outputs, trajectory_size,
    delta):
    num_vars = model_inputs.shape[1]
    num_rows = model_inputs.shape[0]
    num_trajectories = int(num_rows / trajectory_size)
    ee = np.zeros((num_trajectories, num_vars), dtype=np.float)
    ip_vec = model_inputs.reshape(num_trajectories, trajectory_size, num_vars)
    ip_cha = np.subtract(ip_vec[:, 1:, :], ip_vec[:, 0:-1, :])
    up = ip_cha > 0
    lo = ip_cha < 0
    op_vec = model_outputs.reshape(num_trajectories, trajectory_size)
    result_up = get_increased_values(op_vec, up, lo)
    result_lo = get_decreased_values(op_vec, up, lo)
    ee = np.subtract(result_up, result_lo)
    np.divide(ee, delta, out=ee)
    return ee