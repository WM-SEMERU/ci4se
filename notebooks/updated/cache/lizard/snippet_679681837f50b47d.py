def update_memo_key(self, key, account=None, **kwargs):
    if not account:
        if 'default_account' in self.config:
            account = self.config['default_account']
    if not account:
        raise ValueError('You need to provide an account')
    PublicKey(key, prefix=self.prefix)
    account = Account(account, blockchain_instance=self)
    account['options']['memo_key'] = key
    op = operations.Account_update(**{'fee': {'amount': 0, 'asset_id':
        '1.3.0'}, 'account': account['id'], 'new_options': account[
        'options'], 'extensions': {}, 'prefix': self.prefix})
    return self.finalizeOp(op, account['name'], 'active', **kwargs)