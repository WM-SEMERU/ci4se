async def info(self, token):
    token_id = extract_attr(token, keys=['ID'])
    response = await self._api.get('/v1/acl/info', token_id)
    meta = extract_meta(response.headers)
    try:
        result = decode_token(response.body[0])
    except IndexError:
        raise NotFound(response.body, meta=meta)
    return consul(result, meta=meta)