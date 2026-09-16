def get_reachable_volume_templates(self, start=0, count=-1, filter='',
    query='', sort='', networks=None, scope_uris='', private_allowed_only=False
    ):
    uri = self.URI + '/reachable-volume-templates'
    uri += '?networks={}&privateAllowedOnly={}'.format(networks,
        private_allowed_only)
    get_uri = self._client.build_query_uri(start=start, count=count, filter
        =filter, query=query, sort=sort, uri=uri, scope_uris=scope_uris)
    return self._client.get(get_uri)