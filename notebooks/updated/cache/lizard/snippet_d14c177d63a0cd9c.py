def post_vars(self):
    if self.method() != 'POST':
        raise RuntimeError('Unable to return post vars for non-get method')
    content_type = self.content_type()
    if content_type is None or content_type.lower(
        ) != 'application/x-www-form-urlencoded':
        raise RuntimeError(
            'Unable to return post vars with invalid content-type request')
    request_data = self.request_data()
    request_data = request_data.decode() if request_data is not None else ''
    re_search = WWebRequestProto.post_vars_re.search(request_data)
    if re_search is not None:
        return urllib.parse.parse_qs(re_search.group(1), keep_blank_values=1)