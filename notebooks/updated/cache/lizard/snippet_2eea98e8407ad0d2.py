def unix_line_discard(event):
    buff = event.current_buffer
    if (buff.document.cursor_position_col == 0 and buff.document.
        cursor_position > 0):
        buff.delete_before_cursor(count=1)
    else:
        deleted = buff.delete_before_cursor(count=-buff.document.
            get_start_of_line_position())
        event.cli.clipboard.set_text(deleted)