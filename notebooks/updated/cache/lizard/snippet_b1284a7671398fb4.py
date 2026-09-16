def roc_calculator(screened_molecules, status_field, active_label, decoy_label
    ):
    P = 0
    N = 0
    tpf = []
    tpf.append(0)
    fpf = []
    fpf.append(0)
    fpindex = []
    for index in range(len(screened_molecules)):
        if screened_molecules[index].GetProp(status_field
            ) == active_label and index == 0:
            tpf[index] = float(1)
            P = P + 1
            fpindex.append(0)
        elif screened_molecules[index].GetProp(status_field
            ) == active_label and index > 0:
            tpf.append(float(tpf[index - 1] + 1))
            fpf.append(float(fpf[index - 1]))
            P = P + 1
            fpindex.append(0)
        elif screened_molecules[index].GetProp(status_field
            ) == decoy_label and index == 0:
            fpf[index] = float(1)
            N = N + 1
            fpindex.append(1)
        elif screened_molecules[index].GetProp(status_field
            ) == decoy_label and index > 0:
            fpf.append(float(fpf[index - 1] + 1))
            tpf.append(float(tpf[index - 1]))
            N = N + 1
            fpindex.append(1)
    for index in range(len(tpf)):
        tpf[index] = tpf[index] / P
        fpf[index] = fpf[index] / N
    return tpf, fpf, P, N