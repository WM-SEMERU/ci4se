def send(self, content=None, *, wait=False, username=None, avatar_url=None,
    tts=False, file=None, files=None, embed=None, embeds=None):
    payload = {}
    if files is not None and file is not None:
        raise InvalidArgument('Cannot mix file and files keyword arguments.')
    if embeds is not None and embed is not None:
        raise InvalidArgument('Cannot mix embed and embeds keyword arguments.')
    if embeds is not None:
        if len(embeds) > 10:
            raise InvalidArgument('embeds has a maximum of 10 elements.')
        payload['embeds'] = [e.to_dict() for e in embeds]
    if embed is not None:
        payload['embeds'] = [embed.to_dict()]
    if content is not None:
        payload['content'] = str(content)
    payload['tts'] = tts
    if avatar_url:
        payload['avatar_url'] = str(avatar_url)
    if username:
        payload['username'] = username
    return self._adapter.execute_webhook(wait=wait, file=file, files=files,
        payload=payload)