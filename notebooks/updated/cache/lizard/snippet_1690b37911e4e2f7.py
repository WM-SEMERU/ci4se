def get_user_dn(self, username):
    server = ldap3.Server('ldap://' + self.ldap_server)
    connection = ldap3.Connection(server)
    connection.open()
    connection.search(search_base=self.dn, search_filter='(' + self.
        user_attr + '=' + username + ')')
    return connection.response[0]['dn']