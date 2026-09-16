def batch_delete_attributes(self, domain_or_name, items):
    domain, domain_name = self.get_domain_and_name(domain_or_name)
    params = {'DomainName': domain_name}
    self._build_batch_list(params, items, False)
    return self.get_status('BatchDeleteAttributes', params, verb='POST')