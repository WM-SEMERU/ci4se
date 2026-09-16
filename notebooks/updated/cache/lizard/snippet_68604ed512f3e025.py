def get_vault_form_for_create(self, vault_record_types):
    if self._catalog_session is not None:
        return self._catalog_session.get_catalog_form_for_create(
            catalog_record_types=vault_record_types)
    for arg in vault_record_types:
        if not isinstance(arg, ABCType):
            raise errors.InvalidArgument(
                'one or more argument array elements is not a valid OSID Type')
    if vault_record_types == []:
        result = objects.VaultForm(runtime=self._runtime,
            effective_agent_id=self.get_effective_agent_id(), proxy=self._proxy
            )
    else:
        result = objects.VaultForm(record_types=vault_record_types, runtime
            =self._runtime, effective_agent_id=self.get_effective_agent_id(
            ), proxy=self._proxy)
    self._forms[result.get_id().get_identifier()] = not CREATED
    return result