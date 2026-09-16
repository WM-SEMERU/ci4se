def save_site(self, create=True):
    self._load_sites()
    if create:
        self.sites.append(self.site_name)
    task.save_new_site(self.site_name, self.sitedir, self.target, self.port,
        self.address, self.site_url, self.passwords)