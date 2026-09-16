def get_live_scores(self, use_12_hour_format):
    req = requests.get(RequestHandler.LIVE_URL)
    if req.status_code == requests.codes.ok:
        scores_data = []
        scores = req.json()
        if len(scores['games']) == 0:
            click.secho('No live action currently', fg='red', bold=True)
            return
        for score in scores['games']:
            d = {}
            d['homeTeam'] = {'name': score['homeTeamName']}
            d['awayTeam'] = {'name': score['awayTeamName']}
            d['score'] = {'fullTime': {'homeTeam': score['goalsHomeTeam'],
                'awayTeam': score['goalsAwayTeam']}}
            d['league'] = score['league']
            d['time'] = score['time']
            scores_data.append(d)
        self.writer.live_scores(scores_data)
    else:
        click.secho('There was problem getting live scores', fg='red', bold
            =True)