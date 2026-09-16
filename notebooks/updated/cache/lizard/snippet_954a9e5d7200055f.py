def accounts(self):
    response = self.graph.get('%s/accounts' % self.id)
    accounts = []
    for item in response['data']:
        account = Structure(page=Page(id=item['id'], name=item['name'],
            category=item['category']), access_token=item['access_token'],
            permissions=item['perms'])
        accounts.append(account)
    return accounts