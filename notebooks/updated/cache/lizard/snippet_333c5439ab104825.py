def init_realms(self, realms):
    self.realms = tuple(realm for realm in realms if isinstance(realm,
        realm_abcs.AuthorizingRealm))
    self.register_cache_clear_listener()