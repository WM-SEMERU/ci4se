def clean_data(freqs, data, chunk, avg_bin):
    if avg_bin >= chunk:
        raise ValueError(
            'The bin size for averaging the inner product must be less than the chunk size.'
            )
    if chunk >= data.duration:
        raise ValueError('The chunk size must be less than the data duration.')
    steps = numpy.arange(0, int(data.duration / chunk) - 0.5, 0.5)
    seglen = chunk * data.sample_rate
    tref = float(data.start_time)
    for freq in freqs:
        for step in steps:
            start, end = int(step * seglen), int((step + 1) * seglen)
            chunk_line = matching_line(freq, data[start:end], tref,
                bin_size=avg_bin)
            hann_window = numpy.hanning(len(chunk_line))
            apply_hann = TimeSeries(numpy.ones(len(chunk_line)), delta_t=
                chunk_line.delta_t, epoch=chunk_line.start_time)
            if step == 0:
                apply_hann.data[len(hann_window) / 2:] *= hann_window[len(
                    hann_window) / 2:]
            elif step == steps[-1]:
                apply_hann.data[:len(hann_window) / 2] *= hann_window[:len(
                    hann_window) / 2]
            else:
                apply_hann.data *= hann_window
            chunk_line.data *= apply_hann.data
            data.data[start:end] -= chunk_line.data.real
    return data