def on_add(self, widget, data=None):
    if isinstance(self.model, ContainerStateModel):
        try:
            scoped_var_ids = (gui_helper_state_machine.
                add_scoped_variable_to_selected_states(selected_states=[
                self.model]))
            if scoped_var_ids:
                self.select_entry(scoped_var_ids[self.model.state])
        except ValueError as e:
            logger.warning("The scoped variable couldn't be added: {0}".
                format(e))
            return False
        return True