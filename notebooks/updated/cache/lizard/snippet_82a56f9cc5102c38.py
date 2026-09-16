def comment_out_line(filename, line, comment='#'):
    return comment_out_local(filename, line, comment, update_or_append_line
        =update_or_append_line)