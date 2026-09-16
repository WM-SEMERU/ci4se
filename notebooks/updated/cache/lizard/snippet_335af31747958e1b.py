def tachogram(data, sample_rate, signal=False, in_seconds=False,
    out_seconds=False):
    if signal is False:
        data_copy = data
        time_axis = numpy.array(data)
        if out_seconds is True and in_seconds is False:
            time_axis = time_axis / sample_rate
    else:
        data_copy = detect_r_peaks(data, sample_rate, time_units=
            out_seconds, volts=False, resolution=None, plot_result=False)[0]
        time_axis = data_copy
    tachogram_data = numpy.diff(time_axis)
    tachogram_time = time_axis[1:]
    return tachogram_data, tachogram_time