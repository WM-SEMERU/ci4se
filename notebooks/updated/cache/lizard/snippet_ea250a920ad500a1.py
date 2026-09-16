def l1_log_loss(event_times, predicted_event_times, event_observed=None):
    r
    if event_observed is None:
        event_observed = np.ones_like(event_times)
    ix = event_observed.astype(bool)
    return np.abs(np.log(event_times[ix]) - np.log(predicted_event_times[ix])
        ).mean()