def get_account_funds(self, wallet=None):
    return self.make_api_request('Account', 'getAccountFunds', utils.
        get_kwargs(locals()), model=models.AccountFundsResponse)