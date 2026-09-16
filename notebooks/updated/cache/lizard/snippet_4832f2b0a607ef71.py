def gethosts(self):
    self.hosts = get_ip_scope_hosts(self.auth, self.url, self.id)