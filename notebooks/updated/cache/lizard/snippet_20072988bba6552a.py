def lunarEclipseGlobal(jd, backward):
    sweList = swisseph.lun_eclipse_when(jd, backward=backward)
    return {'maximum': sweList[1][0], 'partial_begin': sweList[1][2],
        'partial_end': sweList[1][3], 'totality_begin': sweList[1][4],
        'totality_end': sweList[1][5], 'penumbral_begin': sweList[1][6],
        'penumbral_end': sweList[1][7]}