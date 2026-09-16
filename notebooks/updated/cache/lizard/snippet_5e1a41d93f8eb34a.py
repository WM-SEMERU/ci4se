def eeg_name_frequencies(freqs):
    freqs = list(freqs)
    freqs_names = []
    for freq in freqs:
        if freq < 1:
            freqs_names.append('UltraLow')
        elif freq <= 3:
            freqs_names.append('Delta')
        elif freq <= 7:
            freqs_names.append('Theta')
        elif freq <= 9:
            freqs_names.append('Alpha1/Mu')
        elif freq <= 12:
            freqs_names.append('Alpha2/Mu')
        elif freq <= 13:
            freqs_names.append('Beta1/Mu')
        elif freq <= 17:
            freqs_names.append('Beta1')
        elif freq <= 30:
            freqs_names.append('Beta2')
        elif freq <= 40:
            freqs_names.append('Gamma1')
        elif freq <= 50:
            freqs_names.append('Gamma2')
        else:
            freqs_names.append('UltraHigh')
    return freqs_names