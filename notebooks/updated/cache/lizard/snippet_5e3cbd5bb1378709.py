def put(self, deposit_account_id, amount, receipt):
    return self.connection.put('account/transfer/deposit', data=dict(
        deposit_account_id=deposit_account_id, amount=amount, receipt=receipt))