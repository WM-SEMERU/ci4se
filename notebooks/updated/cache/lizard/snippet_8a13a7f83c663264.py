def Fierz_to_Bern_nunu(C, ddll):
    ind = ddll.replace('l_', '').replace('nu_', '')
    dic = {('nu1' + ind): C['F' + ind + 'nu'], ('nu1p' + ind): C['F' + ind +
        'nup']}
    return dic