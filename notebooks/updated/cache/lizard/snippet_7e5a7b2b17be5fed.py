def connection_info_and_slot(target_node_info):
    slot = None
    if isinstance(target_node_info, dict):
        target_node_info = target_node_info.copy()
        slot = target_node_info.pop('slot', None)
        if list(target_node_info) == ['connection_string']:
            target_node_info = target_node_info['connection_string']
    connection_info = pgutil.get_connection_info(target_node_info)
    return connection_info, slot