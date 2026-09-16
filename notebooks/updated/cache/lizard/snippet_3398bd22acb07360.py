def compstat(sdat, tstart=None, tend=None):
    data = sdat.tseries_between(tstart, tend)
    time = data['t'].values
    delta_time = time[-1] - time[0]
    data = data.iloc[:, 1:].values
    mean = np.trapz(data, x=time, axis=0) / delta_time
    rms = np.sqrt(np.trapz((data - mean) ** 2, x=time, axis=0) / delta_time)
    with open(misc.out_name('statistics.dat'), 'w') as out_file:
        mean.tofile(out_file, sep=' ', format='%10.5e')
        out_file.write('\n')
        rms.tofile(out_file, sep=' ', format='%10.5e')
        out_file.write('\n')