def team_pitching_bref(team, start_season, end_season=None):
    if start_season is None:
        raise ValueError(
            'You need to provide at least one season to collect data for. Try team_pitching_bref(season) or team_pitching_bref(start_season, end_season).'
            )
    if end_season is None:
        end_season = start_season
    url = 'https://www.baseball-reference.com/teams/{}'.format(team)
    data = []
    headings = None
    for season in range(start_season, end_season + 1):
        print('Getting Pitching Data: {} {}'.format(season, team))
        stats_url = '{}/{}.shtml'.format(url, season)
        response = requests.get(stats_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all('table', {'id': 'team_pitching'})[0]
        if headings is None:
            headings = [row.text.strip() for row in table.find_all('th')[1:34]]
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            cols = [col.replace('*', '').replace('#', '') for col in cols]
            cols = [col for col in cols if 'Totals' not in col and 
                'NL teams' not in col and 'AL teams' not in col]
            cols.insert(2, season)
            data.append([ele for ele in cols[0:]])
    headings.insert(2, 'Year')
    data = pd.DataFrame(data=data, columns=headings)
    data = data.dropna()
    return data