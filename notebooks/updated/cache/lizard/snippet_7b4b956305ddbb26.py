def model_changed(self, model, prop_name, info):
    if 'after' in info and self.state == info['instance']:
        self.update_models(model, prop_name, info)
    no_save_change = info['method_name'
        ] in BY_EXECUTION_TRIGGERED_OBSERVABLE_STATE_METHODS
    if isinstance(model, AbstractStateModel
        ) and prop_name == 'state' and no_save_change:
        pass
    elif 'after' in info and info['method_name'
        ] not in BY_EXECUTION_TRIGGERED_OBSERVABLE_STATE_METHODS:
        self._mark_state_machine_as_dirty()
    changed_list = None
    cause = None
    if isinstance(model, DataPortModel) and model.parent is self:
        if model in self.input_data_ports:
            changed_list = self.input_data_ports
            cause = 'input_data_port_change'
        elif model in self.output_data_ports:
            changed_list = self.output_data_ports
            cause = 'output_data_port_change'
    elif isinstance(info.instance, Income) and self is model.parent:
        changed_list = self.income
        cause = 'income_change'
    elif isinstance(info.instance, Outcome) and self is model.parent:
        changed_list = self.outcomes
        cause = 'outcome_change'
    if not (cause is None or cause is 'income_change' or changed_list is None):
        if 'before' in info:
            changed_list._notify_method_before(self.state, cause, (self.
                state,), info)
        elif 'after' in info:
            changed_list._notify_method_after(self.state, cause, None, (
                self.state,), info)
    super(StateModel, self).model_changed(model, prop_name, info)