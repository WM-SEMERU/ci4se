def batch_put_attributes(self, domain_or_name, items, replace=True):
    domain, domain_name = self.get_domain_and_name(domain_or_name)
    params = {'DomainName': domain_name}
    self._build_batch_list(params, items, replace)
    return self.get_status('BatchPutAttributes', params, verb='POST')