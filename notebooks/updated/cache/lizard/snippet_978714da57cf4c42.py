def score_(self):
    if hasattr(self, '_predicted_median'):
        self._concordance_score_ = concordance_index(self.durations, self.
            _predicted_median, self.event_observed)
        del self._predicted_median
        return self._concordance_score_
    return self._concordance_score_