def recent_all_projects(self, limit=30, offset=0):
    method = 'GET'
    url = ('/recent-builds?circle-token={token}&limit={limit}&offset={offset}'
        .format(token=self.client.api_token, limit=limit, offset=offset))
    json_data = self.client.request(method, url)
    return json_data