def handle_set(msg):
    if not msg.gateway.is_sensor(msg.node_id, msg.child_id):
        return None
    msg.gateway.sensors[msg.node_id].set_child_value(msg.child_id, msg.
        sub_type, msg.payload)
    if msg.gateway.sensors[msg.node_id].new_state:
        msg.gateway.sensors[msg.node_id].set_child_value(msg.child_id, msg.
            sub_type, msg.payload, children=msg.gateway.sensors[msg.node_id
            ].new_state)
    msg.gateway.alert(msg)
    if msg.gateway.sensors[msg.node_id].reboot:
        return msg.copy(child_id=SYSTEM_CHILD_ID, type=msg.gateway.const.
            MessageType.internal, ack=0, sub_type=msg.gateway.const.
            Internal.I_REBOOT, payload='')
    return None