def update_results(self, results):
    if not results:
        raise PickerResultException('Results unavailable')
    if results['sequence'] != self.sequence or results['season'
        ] != self.season:
        raise PickerResultException('Results not updated, wrong season or week'
            )
    completed = {g['home']: g for g in results['games'] if g['status'].
        startswith('F')}
    if not completed:
        return 0, None
    count = 0
    for game in self.games.incomplete(home__abbr__in=completed.keys()):
        result = completed.get(game.home.abbr, None)
        if result:
            winner = result['winner']
            game.winner = (game.home if game.home.abbr == winner else game.
                away if game.away.abbr == winner else None)
            count += 1
    last_game = self.last_game
    if not self.points and last_game.winner:
        now = datetime_now()
        if now > last_game.end_time:
            result = completed.get(last_game.home.abbr, None)
            if result:
                self.points = result['home_score'] + result['away_score']
                self.save()
    if count:
        self.update_pick_status()
    return count, self.points