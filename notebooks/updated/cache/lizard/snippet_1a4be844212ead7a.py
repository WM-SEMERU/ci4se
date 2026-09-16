def acquire_account(self, account=None, owner=None):
    if account is not None:
        for _, pool in self.pools:
            if pool.has_account(account):
                return pool.acquire_account(account, owner)
        if not self.default_pool.has_account(account):
            account.acquire()
            return account
    return self.default_pool.acquire_account(account, owner)