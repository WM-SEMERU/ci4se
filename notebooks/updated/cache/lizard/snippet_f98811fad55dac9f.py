def execute(self, state, inputs=None, outputs=None, backward_execution=False):
    if not outputs:
        outputs = {}
    if not inputs:
        inputs = {}
    if backward_execution:
        if hasattr(self._compiled_module, 'backward_execute'):
            return self._compiled_module.backward_execute(state, inputs,
                outputs, rafcon.core.singleton.global_variable_manager)
        else:
            logger.debug('No backward execution method found for state %s' %
                state.name)
            return None
    else:
        return self._compiled_module.execute(state, inputs, outputs, rafcon
            .core.singleton.global_variable_manager)