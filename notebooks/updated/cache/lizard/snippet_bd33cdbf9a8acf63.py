def survival_function_at_times(self, times, label=None):
    label = coalesce(label, self._label)
    return pd.Series(self._survival_function(self._fitted_parameters_,
        times), index=_to_array(times), name=label)