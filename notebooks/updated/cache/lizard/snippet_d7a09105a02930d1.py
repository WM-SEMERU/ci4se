def Refresh(self, location=None):
    if not location:
        location = clc.v2.Account.GetLocation(session=self.session)
    new_object = clc.v2.API.Call('GET', 
        '/v2-experimental/networks/%s/%s/%s' % (self.alias, location, self.
        id), session=self.session)
    if new_object:
        self.name = new_object['name']
        self.data = new_object