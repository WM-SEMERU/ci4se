def _parse_game_data(self, uri):
    boxscore = self._retrieve_html_page(uri)
    if not boxscore:
        return
    fields_to_special_parse = ['away_even_strength_assists',
        'away_power_play_assists', 'away_short_handed_assists',
        'away_game_winning_goals', 'away_saves', 'away_save_percentage',
        'away_shutout', 'home_even_strength_assists',
        'home_power_play_assists', 'home_short_handed_assists',
        'home_game_winning_goals', 'home_saves', 'home_save_percentage',
        'home_shutout']
    for field in self.__dict__:
        short_field = str(field)[1:]
        if (short_field == 'winner' or short_field == 'winning_name' or 
            short_field == 'winning_abbr' or short_field == 'losing_name' or
            short_field == 'losing_abbr' or short_field == 'uri' or 
            short_field == 'date' or short_field == 'time' or short_field ==
            'arena' or short_field == 'attendance' or short_field ==
            'time_of_day' or short_field == 'duration'):
            continue
        if short_field == 'away_name' or short_field == 'home_name':
            value = self._parse_name(short_field, boxscore)
            setattr(self, field, value)
            continue
        if short_field in fields_to_special_parse:
            scheme = BOXSCORE_SCHEME[short_field]
            value = [i.text() for i in boxscore(scheme).items()]
            setattr(self, field, value)
            continue
        index = 0
        if short_field in BOXSCORE_ELEMENT_INDEX.keys():
            index = BOXSCORE_ELEMENT_INDEX[short_field]
        value = utils._parse_field(BOXSCORE_SCHEME, boxscore, short_field,
            index)
        setattr(self, field, value)
    self._away_skaters = len(boxscore(BOXSCORE_SCHEME['away_skaters']))
    num_away_goalies = boxscore(BOXSCORE_SCHEME['away_goalies']).items()
    next(num_away_goalies)
    self._away_goalies = len(next(num_away_goalies)('tbody tr'))
    self._parse_game_date_and_location(boxscore)
    self._away_players, self._home_players = self._find_players(boxscore)