def ldap_server_definitions(self):
    if not self._ldap_server_definitions:
        self._ldap_server_definitions = LdapServerDefinitionManager(self)
    return self._ldap_server_definitions