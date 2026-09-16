def get_projected_player_game_stats_by_player(self, season, week, player_id):
    result = self._method_call(
        'PlayerGameProjectionStatsByPlayerID/{season}/{week}/{player_id}',
        'projections', season=season, week=week, player_id=player_id)
    return result