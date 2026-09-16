def delete_session(sid_s):
    _sessionstore.delete(sid_s)
    with db.session.begin_nested():
        SessionActivity.query.filter_by(sid_s=sid_s).delete()
    return 1