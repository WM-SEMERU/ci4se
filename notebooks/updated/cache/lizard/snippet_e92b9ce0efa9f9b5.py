def organizations(self):
    if self.api and self.organization_ids:
        return self.api._get_organizations(self.organization_ids)