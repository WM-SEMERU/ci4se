def convert_to_LHC(imt):
    if isinstance(imt, SA):
        t = imt.period
    else:
        t = 0.01
    T1 = 0.08
    T2 = 0.56
    T3 = 4.4
    T4 = 8.7
    R1 = 1.106
    R2 = 1.158
    R3 = 1.178
    R4 = 1.241
    R5 = 1.241
    Ratio = max(R1, max(min(R1 + (R2 - R1) / np.log(T2 / T1) * np.log(t /
        T1), R2 + (R3 - R2) / np.log(T3 / T2) * np.log(t / T2)), min(R3 + (
        R4 - R3) / np.log(T4 / T3) * np.log(t / T3), R5)))
    SF = np.log(Ratio)
    return SF