def create_customer(self, *, full_name, email):
    payload = {'fullName': full_name, 'email': email}
    return self.client._post(self.url + 'customers', json=payload, headers=
        self.get_headers())