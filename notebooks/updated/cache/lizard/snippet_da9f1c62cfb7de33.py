def make_redirect_url(self, path_info, query_args=None, domain_part=None):
    suffix = ''
    if query_args:
        suffix = '?' + self.encode_query_args(query_args)
    return str('%s://%s/%s%s' % (self.url_scheme, self.get_host(domain_part
        ), posixpath.join(self.script_name[:-1].lstrip('/'), url_quote(
        path_info.lstrip('/'), self.map.charset, safe='/:|+')), suffix))