def bind(self, binding, parameters):
    if not binding.isProvisioned():
        binding.parameters = parameters
        creds = self.backend.config.generate_binding_credentials(binding)
        p = self.backend.config.generate_binding_permissions(binding,
            DatabaseUsersPermissionsSpecs(creds['username'], creds['password'])
            )
        try:
            self.backend.atlas.DatabaseUsers.create_a_database_user(p)
        except ErrAtlasConflict:
            pass
        self.backend.storage.store(binding)
        return Binding(BindState.SUCCESSFUL_BOUND, credentials=creds)
    elif binding.parameters == parameters:
        if self.backend.config.isGenerateBindingCredentialsPredictible():
            creds = self.backend.config.generate_binding_credentials(binding)
            return Binding(BindState.IDENTICAL_ALREADY_EXISTS, credentials=
                creds)
        raise ErrBindingAlreadyExists()
    else:
        raise ErrBindingAlreadyExists()