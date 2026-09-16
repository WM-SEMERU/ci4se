def get_proc_outputs(self):
    self._session.complete_rpc()
    results = [None] * len(self._session.output_params.items())
    for key, param in self._session.output_params.items():
        results[key] = param.value
    return results