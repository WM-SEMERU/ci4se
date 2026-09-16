def unindent(buffer, from_row, to_row, count=1):
    current_row = buffer.document.cursor_position_row
    line_range = range(from_row, to_row)

    def transform(text):
        remove = '    ' * count
        if text.startswith(remove):
            return text[len(remove):]
        else:
            return text.lstrip()
    new_text = buffer.transform_lines(line_range, transform)
    buffer.document = Document(new_text, Document(new_text).
        translate_row_col_to_index(current_row, 0))
    buffer.cursor_position += buffer.document.get_start_of_line_position(
        after_whitespace=True)