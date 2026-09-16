def gramm_to_promille(gramm, age, weight, height, sex):
    bw = calculate_bw(age, weight, height, sex)
    return gramm * W / (PB * bw)