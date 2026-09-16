def __getOrganizations(self, web):
    orgsElements = web.find_all('a', {'class': 'avatar-group-item'})
    self.organizations = len(orgsElements)