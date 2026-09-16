def ratio_value_number_to_time_series_length(self, x):
    ratio = feature_calculators.ratio_value_number_to_time_series_length(x)
    logging.debug(
        'ratio value number to time series length by tsfresh calculated')
    return ratio