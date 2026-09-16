def get_epochs(self, time=None, stage=None, qual=None, chan=None, name=None):
    time_cond = True
    stage_cond = True
    qual_cond = True
    valid = []
    for ep in self.epochs:
        if stage:
            stage_cond = ep['stage'] in stage
        if qual:
            qual_cond = ep['quality'] == qual
        if time:
            time_cond = time[0] <= ep['start'] and time[1] >= ep['end']
        if stage_cond and qual_cond and time_cond:
            valid.append(ep)
    return valid