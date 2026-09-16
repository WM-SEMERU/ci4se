def slerp(R1, R2, t1, t2, t_out):
    tau = (t_out - t1) / (t2 - t1)
    return np.slerp_vectorized(R1, R2, tau)