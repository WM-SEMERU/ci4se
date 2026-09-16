def rnd_ins_seq(ins_len, C_R, CP_first_nt):
    nt2num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num2nt = 'ACGT'
    if ins_len == 0:
        return ''
    seq = num2nt[CP_first_nt.searchsorted(np.random.random())]
    ins_len += -1
    while ins_len > 0:
        seq += num2nt[C_R[(nt2num[seq[-1]]), :].searchsorted(np.random.
            random())]
        ins_len += -1
    return seq