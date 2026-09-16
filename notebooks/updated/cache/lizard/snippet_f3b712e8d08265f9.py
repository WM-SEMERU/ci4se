def react_to_event(self, event):
    if not react_to_event(self.view, self.view.editor, event):
        return False
    if (not rafcon.gui.singleton.state_machine_manager_model.
        selected_state_machine_id == self.model.state_machine.state_machine_id
        ):
        return False
    return True