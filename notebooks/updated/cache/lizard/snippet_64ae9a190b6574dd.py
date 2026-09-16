def check(self):
    expected_positions = self._machine.needle_positions
    expected_row_length = self._machine.number_of_needles
    for row_index, row in enumerate(self._rows):
        if len(row) != expected_row_length:
            message = _ROW_LENGTH_ERROR_MESSAGE.format(row_index, len(row),
                expected_row_length)
            raise ValueError(message)
        for needle_index, needle_position in enumerate(row):
            if needle_position not in expected_positions:
                message = _NEEDLE_POSITION_ERROR_MESSAGE.format(row_index,
                    needle_index, repr(needle_position), ', '.join(map(repr,
                    expected_positions)))
                raise ValueError(message)