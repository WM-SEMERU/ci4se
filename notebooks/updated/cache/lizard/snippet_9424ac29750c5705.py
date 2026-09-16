def get_column_cursor_position(self, column):
    line_length = len(self.current_line)
    current_column = self.cursor_position_col
    column = max(0, min(line_length, column))
    return column - current_column