def get_box_score_by_team(self, season, week, team_id):
    result = self._method_call('BoxScoreV3/{season}/{week}/{team_id}',
        'stats', season=season, week=week, team_id=team_id)
    return result