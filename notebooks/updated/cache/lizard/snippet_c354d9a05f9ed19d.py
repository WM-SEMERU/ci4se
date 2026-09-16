def speed(self):
    if self._stalled:
        return 0
    time_sum = 0
    data_len_sum = 0
    for time_diff, data_len in self._samples:
        time_sum += time_diff
        data_len_sum += data_len
    if time_sum:
        return data_len_sum / time_sum
    else:
        return 0