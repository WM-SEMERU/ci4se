def UpdateDNS(self, domain, environment):
    self.dns_set_conf(domain, self.dns.config, environment, self.dns.token)