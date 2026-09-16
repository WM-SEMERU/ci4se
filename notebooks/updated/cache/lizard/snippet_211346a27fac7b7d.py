def get_plaintext(self, id):
    return self.service.get_id(self.base, id, params={'format': 'text'}).text