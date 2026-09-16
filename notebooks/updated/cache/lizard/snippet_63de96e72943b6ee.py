def process(self, input_data, ratio, end_of_input=False, verbose=False):
    from samplerate.lowlevel import src_process
    from samplerate.exceptions import ResamplingError
    input_data = np.require(input_data, requirements='C', dtype=np.float32)
    if input_data.ndim == 2:
        num_frames, channels = input_data.shape
        output_shape = int(num_frames * ratio), channels
    elif input_data.ndim == 1:
        num_frames, channels = input_data.size, 1
        output_shape = int(num_frames * ratio),
    else:
        raise ValueError('rank > 2 not supported')
    if channels != self._channels:
        raise ValueError('Invalid number of channels in input data.')
    output_data = np.empty(output_shape, dtype=np.float32)
    error, input_frames_used, output_frames_gen = src_process(self._state,
        input_data, output_data, ratio, end_of_input)
    if error != 0:
        raise ResamplingError(error)
    if verbose:
        info = (
            'samplerate info:\n{} input frames used\n{} output frames generated\n'
            .format(input_frames_used, output_frames_gen))
        print(info)
    return output_data[:output_frames_gen, :] if channels > 1 else output_data[
        :output_frames_gen]