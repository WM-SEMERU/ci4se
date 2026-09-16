def create(self, num_sites):
    super(Internet, self).create(num_sites)
    for _ in range(0, num_sites):
        self.websites.append(Website())