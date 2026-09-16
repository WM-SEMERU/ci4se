def app_stop(device_id, app_id):
    if not is_valid_app_id(app_id):
        abort(403)
    if not is_valid_device_id(device_id):
        abort(403)
    if device_id not in devices:
        abort(404)
    success = devices[device_id].stop_app(app_id)
    return jsonify(success=success)