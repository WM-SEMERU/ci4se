def rotation_at_time(t, timestamps, rotation_sequence):
    idx = np.flatnonzero(timestamps >= t - 0.0001)[0]
    t0 = timestamps[idx - 1]
    t1 = timestamps[idx]
    tau = (t - t0) / (t1 - t0)
    q1 = rotation_sequence[:, (idx - 1)]
    q2 = rotation_sequence[:, (idx)]
    q = rotations.slerp(q1, q2, tau)
    return q