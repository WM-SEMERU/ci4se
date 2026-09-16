def with_claims(self, additional_claims):
    new_additional_claims = copy.deepcopy(self._additional_claims)
    new_additional_claims.update(additional_claims or {})
    return self.__class__(self._signer, service_account_email=self.
        _service_account_email, scopes=self._scopes, token_uri=self.
        _token_uri, subject=self._subject, project_id=self._project_id,
        additional_claims=new_additional_claims)