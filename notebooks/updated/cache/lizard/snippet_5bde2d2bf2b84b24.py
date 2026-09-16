def teams(self):
    teams = self._teamlist.teams()
    current_teams = set(self._teamobjects.keys())
    new_teams = set(teams.keys())
    added = new_teams - current_teams
    removed = current_teams - new_teams
    for team in removed:
        del self._teamobjects[team]
    for team in added:
        self._teamobjects[team] = GitHubTeam(self._api, self._env, self.
            _org, teams[team], team)
    return self._teamobjects.values()