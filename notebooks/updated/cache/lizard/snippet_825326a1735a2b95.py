def upload(resume, message):
    data_config = DataConfigManager.get_config()
    if not upload_is_resumable(data_config) or not opt_to_resume(resume):
        abort_previous_upload(data_config)
        access_token = AuthConfigManager.get_access_token()
        initialize_new_upload(data_config, access_token, message)
    complete_upload(data_config)