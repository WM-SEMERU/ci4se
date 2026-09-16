def sweep_channels(self, sampling_window_ms, n_sampling_windows_per_channel,
    delay_between_windows_ms, interleave_samples, rms, channel_mask):
    channel_cumsum = np.cumsum(channel_mask)
    n_channels_in_mask = channel_cumsum[-1]
    max_channels_per_call = (self.MAX_PAYLOAD_LENGTH - 4 * 4) / (3 * 2
        ) / n_sampling_windows_per_channel
    self._channel_mask_cache = np.array(channel_mask)
    buffer = np.zeros(4)
    for i in range(int(math.ceil(n_channels_in_mask / max_channels_per_call))):
        ind = np.logical_and(channel_cumsum >= i * max_channels_per_call, 
            channel_cumsum < (i + 1) * max_channels_per_call)
        channel_mask_ = np.zeros(len(self._channel_mask_cache), dtype=int)
        channel_mask_[ind] = self._channel_mask_cache[ind]
        channel_mask_uint8 = uint8_tVector()
        channel_mask_uint8.extend(channel_mask_)
        buffer = buffer[:-4]
        buffer = np.concatenate((buffer, np.array(Base.sweep_channels(self,
            sampling_window_ms, n_sampling_windows_per_channel,
            delay_between_windows_ms, interleave_samples, rms,
            channel_mask_uint8))))
    return self.sweep_channels_buffer_to_feedback_result(buffer)