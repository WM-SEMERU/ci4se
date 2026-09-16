def teardown(self):
    self.device_group.teardown()
    self.trust_domain.teardown()
    self.cluster = None