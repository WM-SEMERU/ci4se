def put(self, account_id, user_id):
    return self.connection.put('account/access', data=dict(account_id=
        account_id, user_id=user_id))