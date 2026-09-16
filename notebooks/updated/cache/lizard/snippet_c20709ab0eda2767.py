def add_transitions_to_closest_sibling_state_from_selected_state():
    task_string = 'create transition'
    sub_task_string = 'to closest sibling state'
    selected_state_m, msg = (
        get_selected_single_state_model_and_check_for_its_parent())
    if selected_state_m is None:
        logger.warning('Can not {0} {1}: {2}'.format(task_string,
            sub_task_string, msg))
        return
    logger.debug('Check to {0} {1} ...'.format(task_string, sub_task_string))
    state = selected_state_m.state
    parent_state = state.parent
    closest_sibling_state_tuple = (gui_helper_meta_data.
        get_closest_sibling_state(selected_state_m, 'outcome'))
    if closest_sibling_state_tuple is None:
        logger.info('Can not {0} {1}: There is no other sibling state.'.
            format(task_string, sub_task_string))
        return
    distance, sibling_state_m = closest_sibling_state_tuple
    to_state = sibling_state_m.state
    from_outcomes = get_all_outcomes_except_of_abort_and_preempt(state)
    from_oc_not_connected = [oc for oc in from_outcomes if not state.parent
        .get_transition_for_outcome(state, oc)]
    if from_oc_not_connected:
        logger.debug('Create transition {0} ...'.format(sub_task_string))
        for from_outcome in from_oc_not_connected:
            parent_state.add_transition(state.state_id, from_outcome.
                outcome_id, to_state.state_id, None)
    else:
        target = remove_transitions_if_target_is_the_same(from_outcomes)
        if target:
            target_state_id, _ = target
            if not target_state_id == to_state.state_id:
                logger.info(
                    'Removed transitions from outcomes {0} because all point to the same target.'
                    .format(sub_task_string.replace('closest ', '')))
                add_transitions_to_closest_sibling_state_from_selected_state()
            else:
                logger.info(
                    'Removed transitions from outcomes {0} because all point to the same target.'
                    .format(sub_task_string))
            return True
        logger.info(
            'Will not {0} {1}: Not clear situation of connected transitions.There will be no transitions to other states be touched.'
            .format(task_string, sub_task_string))
    return True