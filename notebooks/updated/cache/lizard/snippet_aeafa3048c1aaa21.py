def Fierz_to_Bern_chrom(C, dd, parameters):
    e = sqrt(4 * pi * parameters['alpha_e'])
    gs = sqrt(4 * pi * parameters['alpha_s'])
    if dd == 'sb' or dd == 'db':
        mq = parameters['m_b']
    elif dd == 'ds':
        mq = parameters['m_s']
    else:
        KeyError('Not sure what to do with quark mass for flavour {}'.
            format(dd))
    return {('7gamma' + dd): gs ** 2 / e / mq * C['F7gamma' + dd], ('8g' +
        dd): gs / mq * C['F8g' + dd], ('7pgamma' + dd): gs ** 2 / e / mq *
        C['F7pgamma' + dd], ('8pg' + dd): gs / mq * C['F8pg' + dd]}