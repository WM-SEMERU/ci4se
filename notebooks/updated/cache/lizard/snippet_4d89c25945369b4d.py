def _find_blocks(self, converted_table, worksheet, flags, units, block_meta
    =None, start_pos=None, end_pos=None):
    blocks = []
    used_cells = []
    if start_pos == None:
        start_pos = 0, 0
    if end_pos == None:
        end_pos = len(converted_table), max(len(row) for row in converted_table
            )
    for row in converted_table:
        used_cells.append([False] * len(row))
    if not converted_table or all(not row for row in converted_table):
        blocks.append(converted_table)
        self.flag_change(flags, 'error', worksheet=worksheet, message=
            'Empty table')
        return blocks
    block = True
    block_search_start = start_pos
    while block:
        block = self._find_valid_block(converted_table, worksheet, flags,
            units, used_cells, block_search_start, end_pos)
        if block:
            blocks.append(block)
            block_search_start = block.start[0], start_pos[1]
    return blocks