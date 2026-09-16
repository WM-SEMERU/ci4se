def _find_conferences(self, year):
    if not year:
        year = utils._find_year_for_season('ncaaf')
    page = self._pull_conference_page(year)
    if not page:
        output = (
            "Can't pull requested conference page. Ensure the following URL exists: %s"
             % (CONFERENCES_URL % year))
        raise ValueError(output)
    conferences = page('table#conferences tbody tr').items()
    for conference in conferences:
        conference_abbreviation = self._get_conference_id(conference)
        conference_name = conference('td[data-stat="conf_name"]').text()
        teams_dict = Conference(conference_abbreviation, year).teams
        conference_dict = {'name': conference_name, 'teams': teams_dict}
        for team in teams_dict.keys():
            self._team_conference[team] = conference_abbreviation
        self._conferences[conference_abbreviation] = conference_dict