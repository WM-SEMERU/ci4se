def POST(self):
    post = FormsDict()
    if not self.content_type.startswith('multipart/'):
        maxlen = max(0, min(self.content_length, self.MEMFILE_MAX))
        pairs = _parse_qsl(tonat(self.body.read(maxlen), 'latin1'))
        for key, value in pairs[:self.MAX_PARAMS]:
            post[key] = value
        return post
    safe_env = {'QUERY_STRING': ''}
    for key in ('REQUEST_METHOD', 'CONTENT_TYPE', 'CONTENT_LENGTH'):
        if key in self.environ:
            safe_env[key] = self.environ[key]
    args = dict(fp=self.body, environ=safe_env, keep_blank_values=True)
    if py >= (3, 2, 0):
        args['encoding'] = 'ISO-8859-1'
    if NCTextIOWrapper:
        args['fp'] = NCTextIOWrapper(args['fp'], encoding='ISO-8859-1',
            newline='\n')
    data = cgi.FieldStorage(**args)
    for item in (data.list or [])[:self.MAX_PARAMS]:
        post[item.name] = item if item.filename else item.value
    return post