def next_game(self):
    if self.is_over():
        raise dominoes.SeriesOverException(
            'Cannot start a new game - series ended with a score of {} to {}'
            .format(*self.scores))
    result = self.games[-1].result
    if result is None:
        raise dominoes.GameInProgressException(
            'Cannot start a new game - the latest one has not finished!')
    if result.points >= 0:
        self.scores[0] += result.points
    else:
        self.scores[1] -= result.points
    if self.is_over():
        return
    if result.won or pow(-1, result.player) * result.points > 0:
        starting_player = result.player
    elif not result.points:
        starting_player = self.games[-1].starting_player
    else:
        starting_player = dominoes.game.next_player(result.player)
    self.games.append(dominoes.Game.new(starting_player=starting_player))
    return self.games[-1]