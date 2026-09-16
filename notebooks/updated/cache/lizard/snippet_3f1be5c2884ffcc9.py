def _agent_import_failed(trace):


    class _AgentImportFailed(Trainer):
        _name = 'AgentImportFailed'
        _default_config = with_common_config({})

        def _setup(self, config):
            raise ImportError(trace)
    return _AgentImportFailed