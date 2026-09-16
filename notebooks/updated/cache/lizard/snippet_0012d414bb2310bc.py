def grant(self, source_cidr):
    self.manager.api.secgroup_rules.create(self.id, source_cidr)