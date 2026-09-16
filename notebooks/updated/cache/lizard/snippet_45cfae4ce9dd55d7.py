def _retrieve_all_teams(self, year):
    team_data_dict = {}
    if not year:
        year = utils._find_year_for_season('nba')
    doc = pq(SEASON_PAGE_URL % year)
    teams_list = utils._get_stats_table(doc, 'div#all_team-stats-base')
    opp_teams_list = utils._get_stats_table(doc, 'div#all_opponent-stats-base')
    for stats_list in [teams_list, opp_teams_list]:
        team_data_dict = self._add_stats_data(stats_list, team_data_dict)
    for team_data in team_data_dict.values():
        team = Team(team_data['data'], team_data['rank'], year)
        self._teams.append(team)