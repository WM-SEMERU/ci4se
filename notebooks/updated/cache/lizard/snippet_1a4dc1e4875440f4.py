def verification_add(self, domain_resource_id, port, is_ssl):
    data = {'domain_href': self.build_api_path('domains',
        domain_resource_id), 'port': port, 'ssl': 'true' if is_ssl else 'false'
        }
    url = self.build_full_url(self.VERIFICATIONS)
    return self.create_resource(url, data)