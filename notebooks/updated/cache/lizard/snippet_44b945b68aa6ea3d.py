async def on_raw_354(self, message):
    target, identifier = message.params[:2]
    if identifier != WHOX_IDENTIFIER:
        return
    metadata = {'nickname': message.params[4], 'username': message.params[2
        ], 'realname': message.params[6], 'hostname': message.params[3]}
    if message.params[5] != NO_ACCOUNT:
        metadata['identified'] = True
        metadata['account'] = message.params[5]
    self._sync_user(metadata['nickname'], metadata)