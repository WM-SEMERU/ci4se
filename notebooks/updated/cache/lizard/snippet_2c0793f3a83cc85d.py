def save(self, folder):
    if not self.account:
        raise ValueError('%s must have an account' % self.__class__.__name__)
    res = self.account.bulk_create(items=[self], folder=folder,
        message_disposition=SAVE_ONLY)
    if res and isinstance(res[0], Exception):
        raise res[0]
    res = list(self.account.fetch(res))
    if res and isinstance(res[0], Exception):
        raise res[0]
    return res[0]