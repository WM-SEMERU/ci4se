def logout(self):
    warnings.warn('Database.logout() is deprecated', DeprecationWarning,
        stacklevel=2)
    self.client._purge_credentials(self.name)