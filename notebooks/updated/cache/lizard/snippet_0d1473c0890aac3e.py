def lmfe(signal, sampling_frequency, frame_length=0.02, frame_stride=0.01,
    num_filters=40, fft_length=512, low_frequency=0, high_frequency=None):
    feature, frame_energies = mfe(signal, sampling_frequency=
        sampling_frequency, frame_length=frame_length, frame_stride=
        frame_stride, num_filters=num_filters, fft_length=fft_length,
        low_frequency=low_frequency, high_frequency=high_frequency)
    feature = np.log(feature)
    return feature