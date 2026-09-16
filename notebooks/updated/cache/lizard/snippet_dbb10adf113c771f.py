def _k_value_square_reduction(ent_pipe_id, exit_pipe_id, re, f):
    if re < 2500:
        return (1.2 + 160 / re) * (ent_pipe_id / exit_pipe_id) ** 4
    else:
        return (0.6 + 0.48 * f) * (ent_pipe_id / exit_pipe_id) ** 2 * ((
            ent_pipe_id / exit_pipe_id) ** 2 - 1)