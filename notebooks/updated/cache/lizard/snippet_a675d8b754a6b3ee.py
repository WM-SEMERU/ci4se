def get_recently_played_games(self, steamID, count=0, format=None):
    parameters = {'steamid': steamID, 'count': count}
    if format is not None:
        parameters['format'] = format
    url = self.create_request_url(self.interface, 'GetRecentlyPlayedGames',
        1, parameters)
    data = self.retrieve_request(url)
    return self.return_data(data, format=format)