def create_session(cls, session_id, user_id):
    count = SessionModel.count(user_id)
    if count < current_app.config['AUTH']['MAX_SESSIONS']:
        cls.__save_session(session_id, user_id)
        return
    elif count >= current_app.config['AUTH']['MAX_SESSIONS']:
        earliest_session = SessionModel.where_earliest(user_id)
        earliest_session.delete()
        cls.__save_session(session_id, user_id)
        return