def get_user_credentials(self):
    if not os.path.exists(os.path.dirname(self.user_credentials)):
        os.makedirs(os.path.dirname(self.user_credentials))
    credentials = self.store.get()
    needs_to_be_updated = not credentials or credentials.invalid
    if needs_to_be_updated:
        self.get_new_user_credentials()
        credentials = self.store.get()
    return credentials