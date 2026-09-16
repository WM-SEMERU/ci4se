def convert_to_row_table(self, add_units=True):
    rtable = []
    if add_units:
        relavent_units = self.get_relavent_units()
    for row_index in range(self.start[0], self.end[0]):
        for column_index in range(self.start[1], self.end[1]):
            cell = self.table[row_index][column_index]
            if cell != None and isinstance(cell, (int, float, long)):
                titles = self._find_titles(row_index, column_index)
                titles.append(cell)
                if add_units:
                    titles.append(relavent_units.get((row_index, column_index))
                        )
                rtable.append(titles)
    if not rtable:
        for row_index in range(self.start[0], self.end[0]):
            row = []
            rtable.append(row)
            for column_index in range(self.start[1], self.end[1]):
                row.append(self.table[row_index][column_index])
            if add_units:
                row.append(relavent_units.get((row_index, column_index)))
    return rtable