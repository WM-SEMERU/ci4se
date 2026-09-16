def create(self, email, phone, country_code=1, send_install_link_via_sms=False
    ):
    data = {'user': {'email': email, 'cellphone': phone, 'country_code':
        country_code}, 'send_install_link_via_sms': send_install_link_via_sms}
    resp = self.post('/protected/json/users/new', data)
    return User(self, resp)