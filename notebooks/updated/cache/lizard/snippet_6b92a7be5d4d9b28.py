def Bern_to_Fierz_lep(C, ddll):
    ind = ddll.replace('l_', '').replace('nu_', '')
    return {('F' + ind + '9'): C['1' + ind] + 10 * C['3' + ind], ('F' + ind +
        '10'): -6 * C['3' + ind], ('F' + ind + 'S'): C['5' + ind] + 40 * C[
        '9' + ind], ('F' + ind + 'P'): 24 * C['9' + ind], ('F' + ind + 'T'):
        C['7' + ind] / 2 + C['7p' + ind] / 2 - 8 * C['9' + ind] - 8 * C[
        '9p' + ind], ('F' + ind + 'T5'): C['7' + ind] / 2 - C['7p' + ind] /
        2 - 8 * C['9' + ind] + 8 * C['9p' + ind], ('F' + ind + '9p'): C[
        '1p' + ind] + 10 * C['3p' + ind], ('F' + ind + '10p'): 6 * C['3p' +
        ind], ('F' + ind + 'Sp'): C['5p' + ind] + 40 * C['9p' + ind], ('F' +
        ind + 'Pp'): -24 * C['9p' + ind]}