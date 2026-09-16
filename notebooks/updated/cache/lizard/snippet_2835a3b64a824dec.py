def denyMapIdentity(self, subject, vendorSpecific=None):
    response = self.denyMapIdentityResponse(subject, vendorSpecific)
    return self._read_boolean_response(response)