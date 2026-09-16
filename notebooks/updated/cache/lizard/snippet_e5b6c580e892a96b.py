def Update(self, name):
    r = clc.v2.API.Call('PUT', 'antiAffinityPolicies/%s/%s' % (self.alias,
        self.id), {'name': name}, session=self.session)
    self.name = name