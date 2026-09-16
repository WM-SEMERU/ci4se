def remove_member_from_group(self, group_id, user_id):
    url = self.TEAM_MEMBERS_URL % (group_id, user_id)
    connection = Connection(self.token)
    connection.set_url(self.production, url)
    return connection.delete_request()