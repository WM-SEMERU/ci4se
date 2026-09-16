def get_http_info_with_retriever(self, request, retriever=None):
    if retriever is None:
        retriever = self.get_form_data
    urlparts = urlparse.urlsplit(request.url)
    try:
        data = retriever(request)
    except ClientDisconnected:
        data = {}
    return {'url': '%s://%s%s' % (urlparts.scheme, urlparts.netloc,
        urlparts.path), 'query_string': urlparts.query, 'method': request.
        method, 'data': data, 'headers': dict(get_headers(request.environ)),
        'env': dict(get_environ(request.environ))}