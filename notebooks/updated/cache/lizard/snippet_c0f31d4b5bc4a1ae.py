def set_session_info(app, response, **extra):
    session_id = getattr(session, 'sid_s', None)
    if session_id:
        response.headers['X-Session-ID'] = session_id
    if current_user.is_authenticated:
        response.headers['X-User-ID'] = current_user.get_id()