def _convert_flags(self, fromlist, tolist, flaglist, context, numlines):
    toprefix = self._prefix[1]
    sameprefix = self._prefix[2]
    next_id = [''] * len(flaglist)
    next_href = [''] * len(flaglist)
    change_positions, same_positions = change_same_starting_points(flaglist)
    change_positions_set = set(change_positions)
    for numChange, changePos in enumerate(change_positions[:-1]):
        next_id[changePos] = self.NEXT_ID_CHANGE.format(toprefix, numChange)
        next_href[changePos] = self.NEXT_HREF.format(toprefix, numChange + 1)
    for same_block, same_start_pos in enumerate(same_positions):
        same_pos = same_start_pos
        while same_pos < len(flaglist
            ) and same_pos not in change_positions_set:
            next_id[same_pos] = self.NEXT_ID_SAME.format(sameprefix,
                same_block, same_pos - same_start_pos + 1)
            same_pos += 1
        num_same_lines = same_pos - same_start_pos
        if num_same_lines > self.MAX_SAME_LINES_BEFORE_SHOW_HIDE:
            next_href[same_start_pos + 2] = self.SHOW_HIDE_ROWS
            self._last_collapsed = True
    if not flaglist:
        flaglist = [False]
        next_id = ['']
        next_href = ['']
        if context:
            fromlist = [self.NO_DIFFERENCES]
            tolist = fromlist
        else:
            fromlist = tolist = [self.EMPTY_FILE]
    if change_positions:
        pos = change_positions[-1]
        next_id[pos] = self.NEXT_ID_CHANGE.format(toprefix, len(
            change_positions) - 1)
        next_href[pos] = self.NEXT_HREF_TOP.format(toprefix)
    return fromlist, tolist, flaglist, next_href, next_id