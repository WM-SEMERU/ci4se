def destroy_team(self):
    request = self._get_request()
    request.post(url=self.TEAM_DESTROY_URL, get_json=False)