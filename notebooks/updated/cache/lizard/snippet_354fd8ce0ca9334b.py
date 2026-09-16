def logout(session_id, **kwargs):
    hydra_session_object = session.SessionObject({}, validate_key=config.
        get('COOKIES', 'VALIDATE_KEY', 'YxaDbzUUSo08b+'), type='file',
        cookie_expires=True, data_dir=config.get('COOKIES', 'DATA_DIR',
        '/tmp'), file_dir=config.get('COOKIES', 'FILE_DIR', '/tmp/auth'))
    hydra_session = hydra_session_object.get_by_id(session_id)
    if hydra_session is not None:
        hydra_session.delete()
        hydra_session.save()
    return 'OK'