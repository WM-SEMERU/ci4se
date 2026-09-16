def device_connect(device_id):
    success = False
    if device_id in devices:
        devices[device_id].connect()
        success = True
    return jsonify(success=success)