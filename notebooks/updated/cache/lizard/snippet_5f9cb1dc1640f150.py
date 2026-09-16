def get_domain_connect_template_sync_url(self, domain, provider_id,
    service_id, redirect_uri=None, params=None, state=None, group_ids=None):
    if params is None:
        params = {}
    config = self.get_domain_config(domain)
    self.check_template_supported(config, provider_id, service_id)
    if config.urlSyncUX is None:
        raise InvalidDomainConnectSettingsException('No sync URL in config')
    sync_url_format = (
        '{}/v2/domainTemplates/providers/{}/services/{}/apply?domain={}&host={}&{}'
        )
    if redirect_uri is not None:
        params['redirect_uri'] = redirect_uri
    if state is not None:
        params['state'] = state
    if group_ids is not None:
        params['groupId'] = ','.join(group_ids)
    return sync_url_format.format(config.urlSyncUX, provider_id, service_id,
        config.domain_root, config.host, urllib.parse.urlencode(sorted(
        params.items(), key=lambda val: val[0])))