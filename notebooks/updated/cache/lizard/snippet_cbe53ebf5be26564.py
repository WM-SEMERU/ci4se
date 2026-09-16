def _register_endpoints(self, providers):
    url_map = []
    for endp_category in self.endpoints:
        for binding, endp in self.endpoints[endp_category].items():
            valid_providers = '|^'.join(providers)
            parsed_endp = urlparse(endp)
            url_map.append(('(^%s)/\\S+/%s' % (valid_providers, parsed_endp
                .path), functools.partial(self.handle_authn_request,
                binding_in=binding)))
    return url_map