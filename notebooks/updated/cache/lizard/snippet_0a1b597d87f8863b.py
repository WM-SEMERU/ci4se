def _minute_exclusion_tree(self):
    itree = IntervalTree()
    for market_open, early_close in self._minutes_to_exclude():
        start_pos = self._find_position_of_minute(early_close) + 1
        end_pos = self._find_position_of_minute(market_open
            ) + self._minutes_per_day - 1
        data = start_pos, end_pos
        itree[start_pos:end_pos + 1] = data
    return itree