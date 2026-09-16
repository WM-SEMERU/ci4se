def create_withdrawal(self, asset, amount, private_key):
    signable_params = {'blockchain': self.blockchain, 'asset_id': asset,
        'amount': str(self.blockchain_amount[self.blockchain](amount)),
        'timestamp': get_epoch_milliseconds(), 'contract_hash': self.
        contract_hash}
    api_params = self.sign_create_withdrawal_function[self.blockchain](
        signable_params, private_key)
    return self.request.post(path='/withdrawals', json_data=api_params)