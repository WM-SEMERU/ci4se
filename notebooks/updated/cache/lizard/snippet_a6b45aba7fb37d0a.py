def trim_games_since(self, t, max_games=500000):
    latest = self.latest_game_number
    earliest = int(latest - max_games)
    gbt = self.games_by_time(earliest, latest)
    if not gbt:
        utils.dbg('No games between %d and %d' % (earliest, latest))
        return
    most_recent = gbt[-1]
    if isinstance(t, datetime.timedelta):
        target = most_recent[0] - t
    else:
        target = t
    i = bisect.bisect_right(gbt, (target,))
    if i >= len(gbt):
        utils.dbg('Last game is already at %s' % gbt[-1][0])
        return
    when, which = gbt[i]
    utils.dbg('Most recent:  %s  %s' % most_recent)
    utils.dbg('     Target:  %s  %s' % (when, which))
    which = int(which)
    self.delete_row_range(ROW_PREFIX, which, latest)
    self.delete_row_range(ROWCOUNT_PREFIX, which, latest)
    self.latest_game_number = which