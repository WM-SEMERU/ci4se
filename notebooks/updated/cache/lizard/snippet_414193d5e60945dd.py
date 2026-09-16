def dc_remove_signal(self, data_frame):
    mean_signal = np.mean(data_frame.mag_sum_acc)
    data_frame['dc_mag_sum_acc'] = data_frame.mag_sum_acc - mean_signal
    logging.debug('dc remove signal')
    return data_frame