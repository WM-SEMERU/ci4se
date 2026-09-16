def run_snr(self):
    if self.ecc:
        required_kwargs = {'dist_type': self.dist_type, 'initial_cond_type':
            self.initial_cond_type, 'ecc': True}
        input_args = [self.m1, self.m2, self.z_or_dist, self.initial_point,
            self.eccentricity, self.observation_time]
    else:
        required_kwargs = {'dist_type': self.dist_type}
        input_args = [self.m1, self.m2, self.spin_1, self.spin_2, self.
            z_or_dist, self.start_time, self.end_time]
    input_kwargs = {**required_kwargs, **self.general, **self.
        sensitivity_input, **self.snr_input, **self.parallel_input}
    self.final_dict = snr(*input_args, **input_kwargs)
    return