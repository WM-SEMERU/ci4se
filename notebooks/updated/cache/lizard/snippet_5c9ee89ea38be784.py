def make_energy_funnel_data(self, cores=1):
    if not self.parameter_log:
        raise AttributeError(
            'No parameter log data to make funnel, have you ran the optimiser?'
            )
    model_cls = self._params['specification']
    gen_tagged = []
    for gen, models in enumerate(self.parameter_log):
        for model in models:
            gen_tagged.append((model[0], model[1], gen))
    sorted_pps = sorted(gen_tagged, key=lambda x: x[1])
    top_result = sorted_pps[0]
    top_result_model = model_cls(*top_result[0])
    if cores == 1 or sys.platform == 'win32':
        energy_rmsd_gen = map(self.funnel_rebuild, [(x, top_result_model,
            self._params['specification']) for x in sorted_pps[1:]])
    else:
        with futures.ProcessPoolExecutor(max_workers=self._params['processors']
            ) as executor:
            energy_rmsd_gen = executor.map(self.funnel_rebuild, [(x,
                top_result_model, self._params['specification']) for x in
                sorted_pps[1:]])
    return list(energy_rmsd_gen)