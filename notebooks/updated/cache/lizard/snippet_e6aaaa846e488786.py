def generate_threshold_mask(hist):
    masked_array = np.ma.masked_values(hist, 0)
    masked_array = np.ma.masked_greater(masked_array, 10 * np.ma.median(hist))
    logging.info('Masking %d pixel(s)', np.ma.count_masked(masked_array))
    return np.ma.getmaskarray(masked_array)