def revoke_token(self, token, token_type=''):
    if token_type:
        self.handler[token_type].black_list(token)
    else:
        self.handler.black_list(token)