def remove_user(self, group, username):
    try:
        self.lookup_id(group)
    except ldap_tools.exceptions.InvalidResult as err:
        raise err from None
    operation = {'memberUid': [(ldap3.MODIFY_DELETE, [username])]}
    self.client.modify(self.__distinguished_name(group), operation)