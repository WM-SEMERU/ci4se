def ref_frequency(self, context):
    num_chans = self._manager.spectral_window_table.getcol(MS.NUM_CHAN)
    ref_freqs = self._manager.spectral_window_table.getcol(MS.REF_FREQUENCY)
    data = np.hstack(np.repeat(rf, bs) for bs, rf in zip(num_chans, ref_freqs))
    return data.reshape(context.shape).astype(context.dtype)