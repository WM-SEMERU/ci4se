def write_docstring_for_shortcut(self):
    result = self.get_function_definition_from_below_last_line()
    if result is not None:
        __, number_of_lines_of_function = result
        cursor = self.code_editor.textCursor()
        for __ in range(number_of_lines_of_function):
            cursor.movePosition(QTextCursor.PreviousBlock)
        self.code_editor.setTextCursor(cursor)
    cursor = self.code_editor.textCursor()
    self.line_number_cursor = cursor.blockNumber() + 1
    self.write_docstring_at_first_line_of_function()