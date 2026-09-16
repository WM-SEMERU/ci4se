def write_event(catalog):
    f = open('event.dat', 'w')
    for i, event in enumerate(catalog):
        try:
            evinfo = event.origins[0]
        except IndexError:
            raise IOError('No origin')
        try:
            Mag_1 = event.magnitudes[0].mag
        except IndexError:
            Mag_1 = 0.0
        try:
            t_RMS = event.origins[0].quality['standard_error']
        except AttributeError:
            print('No time residual in header')
            t_RMS = 0.0
        f.write(str(evinfo.time.year) + str(evinfo.time.month).zfill(2) +
            str(evinfo.time.day).zfill(2) + '  ' + str(evinfo.time.hour).
            rjust(2) + str(evinfo.time.minute).zfill(2) + str(evinfo.time.
            second).zfill(2) + str(evinfo.time.microsecond)[0:2].zfill(2) +
            '  ' + str(evinfo.latitude).ljust(8, str('0')) + '   ' + str(
            evinfo.longitude).ljust(8, str('0')) + '  ' + str(evinfo.depth /
            1000).rjust(7).ljust(9, str('0')) + '   ' + str(Mag_1) +
            '    0.00    0.00   ' + str(t_RMS).ljust(4, str('0')) + str(i).
            rjust(11) + '\n')
    f.close()
    return