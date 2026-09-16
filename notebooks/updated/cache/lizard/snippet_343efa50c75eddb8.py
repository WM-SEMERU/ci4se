async def unlock(self, key, value, *, flags=None, session):
    value = encode_value(value, flags)
    session_id = extract_attr(session, keys=['ID'])
    response = await self._write(key, value, flags=flags, release=session_id)
    return response.body is True