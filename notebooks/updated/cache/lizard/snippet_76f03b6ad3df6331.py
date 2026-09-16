def get_projected_player_game_stats_by_team(self, season, week, team_id):
    result = self._method_call(
        'PlayerGameProjectionStatsByTeam/{season}/{week}/{team_id}',
        'projections', season=season, week=week, team_id=team_id)
    return result