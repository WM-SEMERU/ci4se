def _format_return_timestamps(self, return_timestamps=None):
    if return_timestamps is None:
        return_timestamps_array = np.arange(self.components.initial_time(),
            self.components.final_time() + self.components.saveper(), self.
            components.saveper(), dtype=np.float64)
    elif inspect.isclass(range) and isinstance(return_timestamps, range):
        return_timestamps_array = np.array(return_timestamps, ndmin=1)
    elif isinstance(return_timestamps, (list, int, float, np.ndarray)):
        return_timestamps_array = np.array(return_timestamps, ndmin=1)
    elif isinstance(return_timestamps, _pd.Series):
        return_timestamps_array = return_timestamps.as_matrix()
    else:
        raise TypeError(
            '`return_timestamps` expects a list, array, pandas Series, or numeric value'
            )
    return return_timestamps_array