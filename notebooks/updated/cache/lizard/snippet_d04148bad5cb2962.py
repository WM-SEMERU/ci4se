def latency_to_consolidated(self, lights_off, duration=5, stage=['NREM2',
    'NREM3']):
    epochs = self.get_epochs()
    if len(stage) > 1:
        for ep in epochs:
            if ep['stage'] in stage:
                ep['stage'] = 'target'
        stage = ['target']
    hypno = [x['stage'] for x in epochs]
    groups = groupby(hypno)
    runs = [(stag, sum(1 for _ in group)) for stag, group in groups]
    idx_start = 0
    for one_stage, n in runs:
        if one_stage in stage and n >= duration * 60 / self.epoch_length:
            break
        idx_start += n
    if idx_start < len(hypno):
        latency = (epochs[idx_start]['start'] - lights_off) / 60
    else:
        latency = nan
    return latency