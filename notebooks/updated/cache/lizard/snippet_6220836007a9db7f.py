def account(self, address):
    endpoint = '/accounts/{account_id}'.format(account_id=address)
    return self.query(endpoint)