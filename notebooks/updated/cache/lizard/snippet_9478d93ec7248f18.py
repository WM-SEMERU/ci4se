def _quantiles(self):
    trials = []
    for trial, state in self._trial_state.items():
        if state.last_score is not None and not trial.is_finished():
            trials.append(trial)
    trials.sort(key=lambda t: self._trial_state[t].last_score)
    if len(trials) <= 1:
        return [], []
    else:
        return trials[:int(math.ceil(len(trials) * PBT_QUANTILE))], trials[int
            (math.floor(-len(trials) * PBT_QUANTILE)):]