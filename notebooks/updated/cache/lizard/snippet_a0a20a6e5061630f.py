def _retrieve_all_teams(self, year):
    team_data_dict = {}
    if not year:
        year = utils._find_year_for_season('ncaaf')
    doc = pq(SEASON_PAGE_URL % year)
    teams_list = utils._get_stats_table(doc, 'div#div_standings')
    offense_doc = pq(OFFENSIVE_STATS_URL % year)
    offense_list = utils._get_stats_table(offense_doc, 'table#offense')
    for stats_list in [teams_list, offense_list]:
        team_data_dict = self._add_stats_data(stats_list, team_data_dict)
    for team_name, team_data in team_data_dict.items():
        team = Team(team_data['data'], self._conferences_dict[team_name.
            lower()], year)
        self._teams.append(team)