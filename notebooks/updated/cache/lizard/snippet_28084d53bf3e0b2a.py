def handle_presentation(msg):
    if msg.child_id == SYSTEM_CHILD_ID:
        sensorid = msg.gateway.add_sensor(msg.node_id)
        if sensorid is None:
            return None
        msg.gateway.sensors[msg.node_id].type = msg.sub_type
        msg.gateway.sensors[msg.node_id].protocol_version = msg.payload
        msg.gateway.sensors[msg.node_id].reboot = False
        msg.gateway.alert(msg)
        return msg
    if not msg.gateway.is_sensor(msg.node_id):
        _LOGGER.error('Node %s is unknown, will not add child %s', msg.
            node_id, msg.child_id)
        return None
    child_id = msg.gateway.sensors[msg.node_id].add_child_sensor(msg.
        child_id, msg.sub_type, msg.payload)
    if child_id is None:
        return None
    msg.gateway.alert(msg)
    return msg