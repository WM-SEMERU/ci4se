def create_group(self, name):
    parameters = {'name': name}
    url = self.TEAM_GROUPS_URL
    connection = Connection(self.token)
    connection.set_url(self.production, url)
    connection.add_params(parameters)
    return connection.post_request()