def get_state_model_by_path(self, path):
    path_elements = path.split('/')
    path_elements.pop(0)
    current_state_model = self.root_state
    for state_id in path_elements:
        if isinstance(current_state_model, ContainerStateModel):
            if state_id in current_state_model.states:
                current_state_model = current_state_model.states[state_id]
            else:
                raise ValueError(
                    "Invalid path: State with id '{}' not found in state with id {}"
                    .format(state_id, current_state_model.state.state_id))
        elif isinstance(current_state_model, LibraryStateModel):
            if state_id == current_state_model.state_copy.state.state_id:
                current_state_model = current_state_model.state_copy
            else:
                raise ValueError(
                    "Invalid path: state id '{}' does not coincide with state id '{}' of state_copy of library state with id '{}'"
                    .format(state_id, current_state_model.state_copy.state.
                    state_id, current_state_model.state.state_id))
        else:
            raise ValueError("Invalid path: State with id '{}' has no children"
                .format(current_state_model.state.state_id))
    return current_state_model