def handle_sketch_version(msg):
    if not msg.gateway.is_sensor(msg.node_id):
        return None
    msg.gateway.sensors[msg.node_id].sketch_version = msg.payload
    msg.gateway.alert(msg)
    return None