def close_debt_position(self, symbol, account=None):
    if not account:
        if 'default_account' in self.blockchain.config:
            account = self.blockchain.config['default_account']
    if not account:
        raise ValueError('You need to provide an account')
    account = Account(account, full=True, blockchain_instance=self.blockchain)
    debts = self.list_debt_positions(account)
    if symbol not in debts:
        raise ValueError('No call position open for %s' % symbol)
    debt = debts[symbol]
    asset = debt['debt']['asset']
    collateral_asset = debt['collateral']['asset']
    op = operations.Call_order_update(**{'fee': {'amount': 0, 'asset_id':
        '1.3.0'}, 'delta_debt': {'amount': int(-float(debt['debt']) * 10 **
        asset['precision']), 'asset_id': asset['id']}, 'delta_collateral':
        {'amount': int(-float(debt['collateral']) * 10 ** collateral_asset[
        'precision']), 'asset_id': collateral_asset['id']},
        'funding_account': account['id'], 'extensions': []})
    return self.blockchain.finalizeOp(op, account['name'], 'active')