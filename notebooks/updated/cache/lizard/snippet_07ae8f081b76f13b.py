def get_fantasy_points(self, match_key):
    fantasy_points_url = (self.api_path_v3 + 'fantasy-match-points/' +
        match_key + '/')
    response = self.get_response(fantasy_points_url)
    return response