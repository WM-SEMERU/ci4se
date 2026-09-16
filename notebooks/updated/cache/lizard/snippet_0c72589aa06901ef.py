def _resolve_credential(self, credential):
    if self._credentials_found_in_instance:
        return
    elif self._credentials_found_in_envars():
        return os.getenv('PAN_' + credential.upper())
    else:
        return self.storage.fetch_credential(credential=credential, profile
            =self.profile)