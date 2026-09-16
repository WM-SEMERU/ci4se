def tab_should_insert_whitespace():
    b = get_app().current_buffer
    before_cursor = b.document.current_line_before_cursor
    return bool(b.text and (not before_cursor or before_cursor.isspace()))