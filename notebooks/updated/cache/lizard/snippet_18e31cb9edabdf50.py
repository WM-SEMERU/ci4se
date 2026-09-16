def set_channel_access(channel=14, access_update_mode='non_volatile',
    alerting=False, per_msg_auth=False, user_level_auth=False, access_mode=
    'always', privilege_update_mode='non_volatile', privilege_level=
    'administrator', **kwargs):
    with _IpmiCommand(**kwargs) as s:
        return s.set_channel_access(channel, access_update_mode, alerting,
            per_msg_auth, user_level_auth, access_mode,
            privilege_update_mode, privilege_level)