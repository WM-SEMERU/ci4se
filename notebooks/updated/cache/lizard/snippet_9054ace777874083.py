def get_undo_redo_list_from_active_trail_history_item_to_version_id(self,
    version_id):
    all_trail_action = [a.version_id for a in self.single_trail_history() if
        a is not None]
    all_active_action = self.get_all_active_actions()
    undo_redo_list = []
    _undo_redo_list = []
    intermediate_version_id = version_id
    if self.with_verbose:
        logger.verbose('Version_id    : {0} in'.format(intermediate_version_id)
            )
        logger.verbose('Active actions: {0} in: {1}'.format(
            all_active_action, intermediate_version_id in all_active_action))
        logger.verbose('Trail actions : {0} in: {1}'.format(
            all_trail_action, intermediate_version_id in all_trail_action))
    if intermediate_version_id not in all_trail_action:
        while intermediate_version_id not in all_trail_action:
            _undo_redo_list.insert(0, (intermediate_version_id, 'redo'))
            intermediate_version_id = self.all_time_history[
                intermediate_version_id].prev_id
        intermediate_goal_version_id = intermediate_version_id
    else:
        intermediate_goal_version_id = version_id
    intermediate_version_id = self.trail_history[self.trail_pointer].version_id
    if self.with_verbose:
        logger.verbose('Version_id    : {0} {1}'.format(
            intermediate_goal_version_id, intermediate_version_id))
        logger.verbose('Active actions: {0} in: {1}'.format(
            all_active_action, intermediate_version_id in all_active_action))
        logger.verbose('Trail actions : {0} in: {1}'.format(
            all_trail_action, intermediate_version_id in all_trail_action))
    if intermediate_goal_version_id in all_active_action:
        while not intermediate_version_id == intermediate_goal_version_id:
            undo_redo_list.append((intermediate_version_id, 'undo'))
            intermediate_version_id = self.all_time_history[
                intermediate_version_id].prev_id
    elif intermediate_goal_version_id in all_trail_action:
        while not intermediate_version_id == intermediate_goal_version_id:
            intermediate_version_id = self.all_time_history[
                intermediate_version_id].next_id
            undo_redo_list.append((intermediate_version_id, 'redo'))
    for elem in _undo_redo_list:
        undo_redo_list.append(elem)
    return undo_redo_list