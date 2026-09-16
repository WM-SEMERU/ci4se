def fit_left_censoring(self, df, duration_col=None, event_col=None,
    ancillary_df=None, show_progress=False, timeline=None, weights_col=None,
    robust=False, initial_point=None, entry_col=None):
    self._censoring_type = CensoringType.LEFT
    df = df.copy()
    T = pass_for_numeric_dtypes_or_raise_array(df.pop(duration_col)).astype(
        float)
    self.durations = T.copy()
    self._fit(self._log_likelihood_left_censoring, df, (None, T.values),
        event_col=event_col, ancillary_df=ancillary_df, show_progress=
        show_progress, timeline=timeline, weights_col=weights_col, robust=
        robust, initial_point=initial_point, entry_col=entry_col)
    return self