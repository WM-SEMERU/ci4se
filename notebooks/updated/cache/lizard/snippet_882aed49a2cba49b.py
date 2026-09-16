def team_profiles(self, team):
    return [Profile(raw) for raw in self._get('team/%s/social_media' % self
        .team_key(team))]