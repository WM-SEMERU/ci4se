def create_enrollment_ticket(self, body):
    return self.client.post(self._url('enrollments/ticket'), data=body)