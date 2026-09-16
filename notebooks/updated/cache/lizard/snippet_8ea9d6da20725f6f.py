def run_slurm(self, steps=None, **kwargs):
    params = self.extra_slurm_params
    params.update(kwargs)
    if 'time' not in params:
        params['time'] = self.default_time
    if 'job_name' not in params:
        params['job_name'] = self.job_name
    if 'email' not in params:
        params['email'] = None
    if 'dependency' not in params:
        params['dependency'] = 'singleton'
    self.slurm_job = LoggedJobSLURM(self.command(steps), base_dir=self.
        parent.p.logs_dir, modules=self.modules, **params)
    return self.slurm_job.run()