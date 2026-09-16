def on_episode_end(self, episode, logs):
    duration = timeit.default_timer() - self.starts[episode]
    metrics = self.metrics[episode]
    if np.isnan(metrics).all():
        mean_metrics = np.array([np.nan for _ in self.metrics_names])
    else:
        mean_metrics = np.nanmean(metrics, axis=0)
    assert len(mean_metrics) == len(self.metrics_names)
    data = list(zip(self.metrics_names, mean_metrics))
    data += list(logs.items())
    data += [('episode', episode), ('duration', duration)]
    for key, value in data:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(value)
    if self.interval is not None and episode % self.interval == 0:
        self.save_data()
    del self.metrics[episode]
    del self.starts[episode]