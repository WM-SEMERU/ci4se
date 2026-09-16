def WriteHuntOutputPluginsStates(self, hunt_id, states, cursor=None):
    columns = ', '.join(_HUNT_OUTPUT_PLUGINS_STATES_COLUMNS)
    placeholders = mysql_utils.Placeholders(2 + len(
        _HUNT_OUTPUT_PLUGINS_STATES_COLUMNS))
    hunt_id_int = db_utils.HuntIDToInt(hunt_id)
    for index, state in enumerate(states):
        query = (
            'INSERT INTO hunt_output_plugins_states (hunt_id, plugin_id, {columns}) VALUES {placeholders}'
            .format(columns=columns, placeholders=placeholders))
        args = [hunt_id_int, index, state.plugin_descriptor.plugin_name]
        if state.plugin_descriptor.plugin_args is None:
            args.append(None)
        else:
            args.append(state.plugin_descriptor.plugin_args.SerializeToString()
                )
        args.append(state.plugin_state.SerializeToString())
        try:
            cursor.execute(query, args)
        except MySQLdb.IntegrityError as e:
            raise db.UnknownHuntError(hunt_id=hunt_id, cause=e)