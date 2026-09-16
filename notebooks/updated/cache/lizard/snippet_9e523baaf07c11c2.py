def _request_auth(self, registry):
    if registry:
        if registry.auth:
            registry.auth.load_dockercfg()
        try:
            self._client_session.login(username=registry.auth.user,
                password=registry.auth.passwd, dockercfg_path=registry.auth
                .config_path, reauth=True if registry.auth.auth_type ==
                'registry_rubber' else False, registry=registry.auth.registry)
        except Exception:
            raise
    else:
        raise Exception('a registry is required when requesting auth.')