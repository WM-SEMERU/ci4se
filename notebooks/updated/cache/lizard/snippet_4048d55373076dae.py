def database(self, name=None):
    if (name == self.current_database or name is None and name != self.
        current_database):
        return self.database_class(self.current_database, self)
    else:
        url = self.con.url
        client_class = type(self)
        new_client = client_class(host=url.host, user=url.username, port=
            url.port, password=url.password, database=name)
        return self.database_class(name, new_client)