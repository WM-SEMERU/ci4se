def derive_temporalnetwork(self, params, update_pipeline=True, tag=None,
    njobs=1, confound_corr_report=True):
    if not njobs:
        njobs = self.njobs
    self.add_history(inspect.stack()[0][3], locals(), 1)
    files = self.get_selected_files(quiet=1)
    confound_files = self.get_selected_files(quiet=1, pipeline='confound')
    if confound_files:
        confounds_exist = True
    else:
        confounds_exist = False
    if not confound_corr_report:
        confounds_exist = False
    if not tag:
        tag = ''
    else:
        tag = 'desc-' + tag
    with ProcessPoolExecutor(max_workers=njobs) as executor:
        job = {executor.submit(self._derive_temporalnetwork, f, i, tag,
            params, confounds_exist, confound_files) for i, f in enumerate(
            files) if f}
        for j in as_completed(job):
            j.result()
    if update_pipeline == True:
        if not self.confound_pipeline and len(self.get_selected_files(quiet
            =1, pipeline='confound')) > 0:
            self.set_confound_pipeline = self.pipeline
        self.set_pipeline('teneto_' + teneto.__version__)
        self.set_pipeline_subdir('tvc')
        self.set_bids_suffix('tvcconn')