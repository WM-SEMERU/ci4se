def get_edit_token(self):
    if not self.edit_token or time.time(
        ) - self.instantiation_time > self.token_renew_period:
        self.generate_edit_credentials()
        self.instantiation_time = time.time()
    return self.edit_token