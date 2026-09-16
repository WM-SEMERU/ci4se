def get_recent_seasons(self):
    recent_seasons_url = self.api_path + 'recent_seasons/'
    response = self.get_response(recent_seasons_url)
    return response