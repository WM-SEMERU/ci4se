def calculate_oobatake_dS(seq, temp):
    seq = ssbio.protein.sequence.utils.cast_to_str(seq)
    dS = 0
    temp += 273.15
    T0 = 298.15
    dCp_sum = _sum_of_dCp(seq)
    for aa in seq:
        S0 = oobatake_dictionary[aa]['dS']
        dS += S0
    return dS + dCp_sum * math.log(temp / T0)