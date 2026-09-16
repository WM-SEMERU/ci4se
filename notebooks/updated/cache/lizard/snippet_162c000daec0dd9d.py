def user_specific_data_directory(user_context):
    return os.path.join(user_context.steam.userdata_directory, user_context
        .user_id)