def removeMapIdentity(self, subject, vendorSpecific=None):
    response = self.removeMapIdentityResponse(subject, vendorSpecific)
    return self._read_boolean_response(response)