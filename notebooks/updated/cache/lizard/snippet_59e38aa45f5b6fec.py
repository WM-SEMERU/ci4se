def calculate_ef_var(tpf, fpf):
    efvara = tpf * (1 - tpf)
    efvard = fpf * (1 - fpf)
    ef = tpf / fpf
    if fpf == 1:
        return 0, 0, 0
    else:
        s = ef * (1 + np.log(ef) / np.log(fpf))
        s2 = s * s
        return efvara, efvard, s2