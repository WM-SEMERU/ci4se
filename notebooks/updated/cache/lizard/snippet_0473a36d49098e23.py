def dataframe(self):
    fields_to_include = {'abbreviation': self.abbreviation, 'conference':
        self.conference, 'conference_losses': self.conference_losses,
        'conference_win_percentage': self.conference_win_percentage,
        'conference_wins': self.conference_wins, 'first_downs': self.
        first_downs, 'first_downs_from_penalties': self.
        first_downs_from_penalties, 'fumbles_lost': self.fumbles_lost,
        'games': self.games, 'interceptions': self.interceptions, 'losses':
        self.losses, 'name': self.name, 'pass_attempts': self.pass_attempts,
        'pass_completion_percentage': self.pass_completion_percentage,
        'pass_completions': self.pass_completions, 'pass_first_downs': self
        .pass_first_downs, 'pass_touchdowns': self.pass_touchdowns,
        'pass_yards': self.pass_yards, 'penalties': self.penalties, 'plays':
        self.plays, 'points_against_per_game': self.points_against_per_game,
        'points_per_game': self.points_per_game, 'rush_attempts': self.
        rush_attempts, 'rush_first_downs': self.rush_first_downs,
        'rush_touchdowns': self.rush_touchdowns, 'rush_yards': self.
        rush_yards, 'rush_yards_per_attempt': self.rush_yards_per_attempt,
        'simple_rating_system': self.simple_rating_system,
        'strength_of_schedule': self.strength_of_schedule, 'turnovers':
        self.turnovers, 'win_percentage': self.win_percentage, 'wins': self
        .wins, 'yards': self.yards, 'yards_from_penalties': self.
        yards_from_penalties, 'yards_per_play': self.yards_per_play}
    return pd.DataFrame([fields_to_include], index=[self._abbreviation])