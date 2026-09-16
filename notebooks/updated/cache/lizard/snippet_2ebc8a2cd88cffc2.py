def fft(ts):
    t_step = ts.index[1] - ts.index[0]
    oc = np.abs(np.fft.fftshift(np.fft.fft(ts.values))) / len(ts.values)
    t = np.fft.fftshift(np.fft.fftfreq(len(oc), d=t_step))
    return Trace(oc, t)