def _kbos_from_survey_sym_model_input_file(model_file):
    lines = storage.open_vos_or_local(model_file).read().split('\n')
    kbos = []
    for line in lines:
        if len(line) == 0 or line[0] == '#':
            continue
        kbo = ephem.EllipticalBody()
        values = line.split()
        kbo.name = values[8]
        kbo.j = values[9]
        kbo.k = values[10]
        kbo._a = float(values[0])
        kbo._e = float(values[1])
        kbo._inc = float(values[2])
        kbo._Om = float(values[3])
        kbo._om = float(values[4])
        kbo._M = float(values[5])
        kbo._H = float(values[6])
        epoch = ephem.date(2453157.5 - ephem.julian_date(0))
        kbo._epoch_M = epoch
        kbo._epoch = epoch
        kbos.append(kbo)
    return kbos