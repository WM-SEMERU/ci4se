def update_witness(self, witness_identifier, url=None, key=None, **kwargs):
    witness = Witness(witness_identifier)
    account = witness.account
    op = operations.Witness_update(**{'fee': {'amount': 0, 'asset_id':
        '1.3.0'}, 'prefix': self.prefix, 'witness': witness['id'],
        'witness_account': account['id'], 'new_url': url, 'new_signing_key':
        key})
    return self.finalizeOp(op, account['name'], 'active', **kwargs)