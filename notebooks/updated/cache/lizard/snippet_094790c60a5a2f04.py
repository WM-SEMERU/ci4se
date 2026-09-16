def user():
    user = flogin.current_user
    return flask.jsonify({'id': user.get_id(), 'name': user.name,
        'is_active': user.is_active(), 'is_anonymous': user.is_anonymous})