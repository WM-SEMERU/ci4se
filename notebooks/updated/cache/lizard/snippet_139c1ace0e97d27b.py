def receive_trial_result(self, parameter_id, parameters, value):
    reward = extract_scalar_reward(value)
    if parameter_id not in self.total_data:
        raise RuntimeError('Received parameter_id not in total_data.')
    params = self.total_data[parameter_id]
    if self.optimize_mode is OptimizeMode.Maximize:
        reward = -reward
    rval = self.rval
    domain = rval.domain
    trials = rval.trials
    new_id = len(trials)
    rval_specs = [None]
    rval_results = [domain.new_result()]
    rval_miscs = [dict(tid=new_id, cmd=domain.cmd, workdir=domain.workdir)]
    vals = params
    idxs = dict()
    out_y = dict()
    json2vals(self.json, vals, out_y)
    vals = out_y
    for key in domain.params:
        if key in [VALUE, INDEX]:
            continue
        if key not in vals or vals[key] is None or vals[key] == []:
            idxs[key] = vals[key] = []
        else:
            idxs[key] = [new_id]
            vals[key] = [vals[key]]
    self.miscs_update_idxs_vals(rval_miscs, idxs, vals, idxs_map={new_id:
        new_id}, assert_all_vals_used=False)
    trial = trials.new_trial_docs([new_id], rval_specs, rval_results,
        rval_miscs)[0]
    trial['result'] = {'loss': reward, 'status': 'ok'}
    trial['state'] = hp.JOB_STATE_DONE
    trials.insert_trial_docs([trial])
    trials.refresh()