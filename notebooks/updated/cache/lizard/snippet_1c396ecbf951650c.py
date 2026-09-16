def write_frames(self, input, nframes=-1):
    if nframes == -1:
        if input.ndim == 1:
            nframes = input.size
        elif input.ndim == 2:
            nframes = input.shape[0]
        else:
            raise ValueError(
                'Input has to be rank 1 (mono) or rank 2 (multi-channels)')
    return self._sndfile.write_frames(input[:nframes, (...)])