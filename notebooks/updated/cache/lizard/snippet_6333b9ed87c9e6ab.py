def push_to_server(self, data):
    output = add_profile(self.customer.pk, data, data)
    output['response'].raise_if_error()
    self.profile_id = output['profile_id']
    self.payment_profile_ids = output['payment_profile_ids']