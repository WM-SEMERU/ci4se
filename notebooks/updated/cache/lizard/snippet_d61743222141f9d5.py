def is_snapshot_time(self, output_every=None, t_output_every=None):
    if t_output_every is not None:
        output_every = int(round(t_output_every // self.model.dt))
    return not self.model.i % output_every