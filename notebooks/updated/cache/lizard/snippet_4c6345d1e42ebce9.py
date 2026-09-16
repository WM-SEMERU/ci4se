def current_app(device_id):
    if not is_valid_device_id(device_id):
        abort(403)
    if device_id not in devices:
        abort(404)
    current = devices[device_id].current_app
    if current is None:
        abort(404)
    return jsonify(current_app=current)