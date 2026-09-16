def delete_domain(self, domain_or_name):
    domain, domain_name = self.get_domain_and_name(domain_or_name)
    params = {'DomainName': domain_name}
    return self.get_status('DeleteDomain', params)