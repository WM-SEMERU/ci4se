def _parse_team_name(self, team):
    team = team.replace('&#160;', ' ')
    team = team.replace('\xa0', ' ')
    team_html = pq(team)
    return team_html.text()