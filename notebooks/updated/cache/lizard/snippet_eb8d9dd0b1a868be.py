def get_account_from_hash(self, account_hash):
    for _, pool in self.pools:
        account = pool.get_account_from_hash(account_hash)
        if account is not None:
            return account
    return self.default_pool.get_account_from_hash(account_hash)