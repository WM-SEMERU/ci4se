def takeout(self, finalize=True, *, contacts=None, users=None, chats=None,
    megagroups=None, channels=None, files=None, max_file_size=None):
    request_kwargs = dict(contacts=contacts, message_users=users,
        message_chats=chats, message_megagroups=megagroups,
        message_channels=channels, files=files, file_max_size=max_file_size)
    arg_specified = (arg is not None for arg in request_kwargs.values())
    if self.session.takeout_id is None or any(arg_specified):
        request = functions.account.InitTakeoutSessionRequest(**request_kwargs)
    else:
        request = None
    return _TakeoutClient(finalize, self, request)