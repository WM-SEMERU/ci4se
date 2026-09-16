def get_aa_letter(aa_code):
    aa_letter = 'X'
    for key, val in standard_amino_acids.items():
        if val == aa_code:
            aa_letter = key
    return aa_letter