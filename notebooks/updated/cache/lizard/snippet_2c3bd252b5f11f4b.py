def get_group(self, group_id):
    url = self.TEAM_GROUPS_ID_URL % group_id
    connection = Connection(self.token)
    connection.set_url(self.production, url)
    return connection.get_request()