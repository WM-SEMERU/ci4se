def create_grupo_virtual(self):
    return GrupoVirtual(self.networkapi_url, self.user, self.password, self
        .user_ldap)