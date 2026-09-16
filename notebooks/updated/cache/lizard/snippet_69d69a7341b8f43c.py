def get_season(self, season_key, card_type='micro_card'):
    season_url = self.api_path + 'season/' + season_key + '/'
    params = {}
    params['card_type'] = card_type
    response = self.get_response(season_url, params)
    return response