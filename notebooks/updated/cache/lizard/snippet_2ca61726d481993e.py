def run_simulations(self, param_list, show_progress=True):
    if self.runner is None:
        raise Exception(
            'No runner was ever specified for this CampaignManager.')
    if param_list == []:
        return
    desired_params = self.db.get_params()
    for p in param_list:
        passed = list(p.keys())
        available = ['RngRun'] + desired_params
        if set(passed) != set(available):
            raise ValueError(
                """Specified parameter combination does not match the supported parameters:
Passed: %s
Supported: %s"""
                 % (sorted(passed), sorted(available)))
    if self.check_repo:
        self.check_repo_ok()
    self.runner.configure_and_build(skip_configuration=True)
    shuffle(param_list)
    results = self.runner.run_simulations(param_list, self.db.get_data_dir())
    if show_progress:
        result_generator = tqdm(results, total=len(param_list), unit=
            'simulation', desc='Running simulations')
    else:
        result_generator = results
    for result in result_generator:
        self.db.insert_result(result)