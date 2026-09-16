def undo(self, key_value, modifier_mask):
    for key, tab in gui_singletons.main_window_controller.get_controller(
        'states_editor_ctrl').tabs.items():
        if tab['controller'].get_controller('source_ctrl'
            ) is not None and react_to_event(self.view, tab['controller'].
            get_controller('source_ctrl').view.textview, (key_value,
            modifier_mask)) or tab['controller'].get_controller(
            'description_ctrl') is not None and react_to_event(self.view,
            tab['controller'].get_controller('description_ctrl').view.
            textview, (key_value, modifier_mask)):
            return False
    if self._selected_sm_model is not None:
        self._selected_sm_model.history.undo()
        return True
    else:
        logger.debug(
            'Undo is not possible now as long as no state_machine is selected.'
            )