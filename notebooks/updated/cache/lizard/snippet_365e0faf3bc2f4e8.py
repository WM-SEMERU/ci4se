def address(self, street, city=None, state=None, zipcode=None, **kwargs):
    fields = {'street': street, 'city': city, 'state': state, 'zip': zipcode}
    return self._fetch('address', fields, **kwargs)