async def _formulate_body(self):
    c_type, body = None, ''
    multipart_ctype = 'multipart/form-data; boundary={}'.format(_BOUNDARY)
    if self.data is not None:
        if self.files or self.json is not None:
            raise TypeError(
                'data arg cannot be used in conjunction withfiles or json arg.'
                )
        c_type = 'application/x-www-form-urlencoded'
        try:
            body = self._dict_to_query(self.data, params=False)
        except AttributeError:
            body = self.data
            c_type = self.mimetype or 'text/plain'
    elif self.files is not None:
        if self.data or self.json is not None:
            raise TypeError(
                'files arg cannot be used in conjunction withdata or json arg.'
                )
        c_type = multipart_ctype
        body = await self._multipart(self.files)
    elif self.json is not None:
        if self.data or self.files:
            raise TypeError(
                'json arg cannot be used in conjunction withdata or files arg.'
                )
        c_type = 'application/json'
        body = _json.dumps(self.json)
    return c_type, str(len(body)), body