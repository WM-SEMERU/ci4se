def get_channel_max_user_count(channel=14, **kwargs):
    access = get_user_access(channel=channel, uid=1, **kwargs)
    return access['channel_info']['max_user_count']