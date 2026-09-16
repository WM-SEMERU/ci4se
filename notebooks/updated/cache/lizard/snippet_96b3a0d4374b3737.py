def hasReservation(self, pid, subject, vendorSpecific=None):
    response = self.hasReservationResponse(pid, subject, vendorSpecific)
    return self._read_boolean_404_response(response)