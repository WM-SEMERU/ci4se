def insert_state_into_selected_state(state, as_template=False):
    smm_m = rafcon.gui.singleton.state_machine_manager_model
    if not isinstance(state, State):
        logger.warning('A state is needed to be insert not {0}'.format(state))
        return False
    if not smm_m.selected_state_machine_id:
        logger.warning(
            'Please select a container state within a state machine first')
        return False
    selection = smm_m.state_machines[smm_m.selected_state_machine_id].selection
    if len(selection.states) > 1:
        logger.warning('Please select exactly one state for the insertion')
        return False
    if len(selection.states) == 0:
        logger.warning('Please select a state for the insertion')
        return False
    if is_selection_inside_of_library_state(selected_elements=[selection.
        get_selected_state()]):
        logger.warning(
            'State is not insert because target state is inside of a library state.'
            )
        return False
    gui_helper_state.insert_state_as(selection.get_selected_state(), state,
        as_template)
    return True