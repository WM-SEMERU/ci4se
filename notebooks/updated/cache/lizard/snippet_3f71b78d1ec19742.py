def create_state_model_for_state(new_state, meta, state_element_models):
    from rafcon.gui.models.abstract_state import get_state_model_class_for_state
    state_m_class = get_state_model_class_for_state(new_state)
    new_state_m = state_m_class(new_state, meta=meta, load_meta_data=False,
        expected_future_models=state_element_models)
    error_msg = 'New state has not re-used all handed expected future models.'
    check_expected_future_model_list_is_empty(new_state_m, msg=error_msg)
    return new_state_m