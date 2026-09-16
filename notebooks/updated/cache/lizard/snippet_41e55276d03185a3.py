def hidden_basic_auth(user='user', passwd='passwd'):
    if not check_basic_auth(user, passwd):
        return status_code(404)
    return jsonify(authenticated=True, user=user)